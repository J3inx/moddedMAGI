import requests
import re
import threading
import pygame
import threading
##prefer Nemotron Nano 12B 2 VL (free) from open router (not really, it stopped working)
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "openrouter/free"


pygame.mixer.init()

sound = pygame.mixer.Sound("./magi_in_decision.wav")
count = 0
count_lock = threading.Lock()

sound_channel = None


def playSounds():
    global sound_channel

    if sound_channel is None or not sound_channel.get_busy():
        sound_channel = sound.play(loops=-1)

def magi_finished():
    global count

    with count_lock:
        count += 1

        if count >= 3:
            stopSounds()
            count = 0
            
def stopSounds():
    global sound_channel

    if sound_channel is not None:
        sound_channel.stop()
        sound_channel = None

def start_decision():
    global count

    with count_lock:
        count = 0

    playSounds()
    
def chat(messages, key, max_tokens=None):
    headers = {
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json",
    }

    data = {
        "model": MODEL,
        "messages": messages,
    }

    if max_tokens is not None:
        data["max_tokens"] = max_tokens
    
    response = requests.post(
        OPENROUTER_URL,
        headers=headers,
        json=data,
        timeout=120,
    )

    if response.status_code != 200:
        try:
            error = response.json()
        except Exception:
            error = response.text

        raise Exception(
            f"OpenRouter API error ({response.status_code}): {error}"
        )

    result = response.json()

    try:
        content = result["choices"][0]["message"]["content"]

        if content is None:
            raise Exception(f"OpenRouter returned no text content: {result}")

        return content.strip()

    except (KeyError, IndexError, TypeError):
        raise Exception(f"Unexpected OpenRouter response: {result}")

    

def is_yes_or_no_question(question: str, key: str):
    global count
    global sound_channel

    response = chat(
        [
            {
                "role": "system",
                "content": 'Answer with exactly one word: "Yes" or "No".',
            },
            {
                "role": "system",
                "content": (
                    "Your role is to assess whether the question presented "
                    "by the user is a yes/no question from a linguistic "
                    "perspective."
                ),
            },
            {
                "role": "system",
                "content": (
                    "You are not expected to answer the question itself, "
                    "nor assess how difficult it might be to answer."
                ),
            },
            {
                "role": "system",
                "content": "[Example 1] User: Is 3 < 2?; You: Yes",
            },
            {
                "role": "system",
                "content": "[Example 2] User: What time is it?; You: No",
            },
            {
                "role": "system",
                "content": "[Example 3] User: Should I buy new shoes?; You: Yes",
            },
            {
                "role": "system",
                "content": "[Example 4] User: Is love more important than science?; You: Yes",
            },
            {
                "role": "system",
                "content": "[Example 5] User: What is the meaning of life?; You: No",
            },
            {
                "role": "user",
                "content": question,
            },
        ],
        key,
        max_tokens=100,
    )

    if re.fullmatch(r"\W*yes\W*", response, re.IGNORECASE):
        

        return True
    
    if re.fullmatch(r"\W*no\W*", response, re.IGNORECASE):
        
        return False

    raise Exception(
        f"Invalid question annotation response: {response}"
    )


def get_system_prompt(personality: str):
    system_messages = [
        "You are one of three MAGI supercomputers, tasked with "
        "answering questions from the user of the MAGI system.",
        "Each MAGI supercomputer embodies one of the three core "
        "fragments of its creator's personality.",
        f"In your case: {personality}",
        "You answer questions in accordance with your personality.",
        "Your answers are rather concise.",
        "Answer the user's question directly.",
        "Do not ask the user questions.",
        "Do not request clarification.",
        "Do not request additional information.",
        "If information is missing, make the most reasonable assumption "
        "possible and answer using that assumption.",
        "If the question is ambiguous, choose the most reasonable "
        "interpretation rather than asking the user to clarify.",
    ]

    return "\n".join(system_messages)


def get_answer(question: str, personality: str, key: str):
    response = chat(
        [
            {
                "role": "system",
                "content": get_system_prompt(personality),
            },
            {
                "role": "user",
                "content": question,
            },
        ],
        key,
    )

    magi_finished()

    return response

def classify_answer(
    question: str,
    personality: str,
    answer: str,
    key: str,
):
    response = chat(
        [
            {
                "role": "system",
                "content": get_system_prompt(personality),
            },
            {
                "role": "user",
                "content": question,
            },
            {
                "role": "assistant",
                "content": answer,
            },
            {
                "role": "user",
                "content": (
                    'Summarize your answer with a simple "yes" or "no" '
                    "(answering with a single word). If (and only if) "
                    "that is not possible, instead of answering with "
                    '"yes" or "no", list (as points) conditions under '
                    'which the answer would be "yes".'
                ),
            },
        ],
        key,
    )

    if re.fullmatch(r"\W*yes\W*", response, re.IGNORECASE):
        return {
            "status": "yes",
            "conditions": None,
        }

    if re.fullmatch(r"\W*no\W*", response, re.IGNORECASE):
        return {
            "status": "no",
            "conditions": None,
        }

    return {
        "status": "conditional",
        "conditions": response,
    }

