[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads)
# Modder's Remarks
This program was originally made by TomaszRewak(https://github.com/TomaszRewak/MAGI), it also originally used the OpenAi api to run but i didn't feel like paying for that so with lots of help from ai I worked on converting it to openRouter instead so it can use the free api keys on the website, i also wanted to replicate the audio played by the magi computer when it was making decisions so i added crappy sounds that i tried to make sound as close to the original as i could as well as a sound ripped from the n64 Evangelion game
below is the original readme file along with some additions i added to let it work properly with the additions i made as well as a screenshot of the guardrails i added to open router as some of the ai's wouldn't work properly or understand the prompts properly
<img width="1256" height="370" alt="Screenshot 2026-08-10 at 09 19 15" src="https://github.com/user-attachments/assets/ab5b7e66-c2c3-4d9f-9d72-208a3274d612" />

the audio files used could use some real work, for the deciding sound i had to use an alarm clock sound pitched up and sped up, and for the decision made sound i used a sound from the Evangelion 64 game, not even sure where it came from since the file names from the library i found are not helpful at all, if anyone has some raw sound effects that aren't muddled like the reference clip below please let me know or replace them in this repository.

Reference audio:
[MAGI refference audio](https://github.com/user-attachments/assets/71fa0248-5739-4111-b1e7-64c9e8c264a1)

Deciding audio:
[MAGI_in_decision.wav](https://github.com/user-attachments/files/30901807/magi_in_decision.wav) 

Decision made audio:
[MAGI decision_made.wav](https://github.com/user-attachments/files/30901772/magi_decision_made.wav)



setup:
if you dont have python 3.11 use ```brew install python@3.11```

then run

```/opt/homebrew/bin/python3.11 -m venv venv``` 

```. venv/bin/activate``` 

```pip install -r requirements.txt``` 

```python main.py```


on my computer i also had problems running the script due to one of the requirements not working properly so i had to install an older version using this code:

```python3 -m pip install "setuptools<81"```

original description by TomaszRewak(https://github.com/TomaszRewak/MAGI):
# MAGI

MAGI system is a cluster of three AI supercomputers that manage and support all task performed by the NERV organization from their Tokyo-3 headquarter.

Originally designed by Dr. Naoko Akagi, each of the three AI agents reflects a separate part of her complex personality:
- MELCHIOR • 1 - her as a scientist,
- BALTHASAR • 2 - her as a mother,
- CASPER • 3 - her as a woman.

Those (often conflicting, yet complementary) agents participate in a voting process in order to answer most challenging questions. 

<p align="center">
  <img src="https://raw.githubusercontent.com/TomaszRewak/MAGI/master/examples/example_1.gif" width=800/>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/TomaszRewak/MAGI/master/examples/example_2.gif" width=800/>
</p>

## Implementation

The presented implementation of the MAGI system is powered by the ChatGPT-3.5 large language model. (Upgrading the model to ChatGPT-4 in the future may bring further improvements in its abilities).

The procedure of answering questions is as follows:
1. The question is classified in order to determine if it can be answered with a "yes"/"no" response.
2. The question (as is) is presented to each MAGI agent.
3. If the question was classified as a "yes"/"no" question, each agent is tasked with classifying their respective answers into one of those two categories (and optionally listing additional conditions if the actual answer is too complex).

The system can produce following responses (that are evaluated in this order):
- error (誤 差) - if one or more agents encountered an error
- info (情 報) - if the question was not classified as a "yes"/"no" question
- no (拒 絶) - if at least one of the agent answered with a "no"
- conditional (状 態) - if at least one agent answered with a conditional "yes"
- yes (合 意) - if all agents answered with an unconditional "yes"

Individual agents can be inspected in order to view their full replies and additional conditions.

Each subsystem was fine-tuned using following prompts:
- MELCHIOR • 1 - You are a scientist. Your goal is to further our understanding of the universe and advance our technological progress.
- BALTHASAR • 2 - You are a mother. Your goal is to protect your children and ensure their well-being.
- CASPER • 3 - You are a woman. Your goal is to pursue love, dreams and desires.

## Usage

*In order to follow those steps, you need `git` and `python` (version 3) installed on your system. The presented steps should work on the Windows OS (for linux systems the process should be similar, but may differ slightly).*

1. Clone the repo:

```
git clone https://github.com/TomaszRewak/MAGI.git
```

2. Navigate to the cloned directory:

```
cd MAGI
```

3. Create python virtual environment:

```
python -m venv .venv
```

4. Activate the virtual environment:

```
.\.venv\scripts\activate
```
5. Install dependencies:

```
pip install -r requirements.txt
```

6. Start the app:

```
python main.py
```
NOTE: the requirements work best with python 3.11.5 so these are the actual commands to run:

```/opt/homebrew/bin/python3.11 -m venv venv```

```. venv/bin/activate```

```pip install -r requirements.txt```

```python main.py```

7. Navigate to http://127.0.0.1:8050/ in your web browser.

8. Paste your openAI API key into the `access code` field (alternatively you can set the `OPENAI_API_KEY` environment variable before starting the app).

NOTE: it is not OpenAi anymore, this program uses openRouter instead as it has a wider variety of free keys

10. Write your question into the `question` field and hit enter.

11. Click on individual subsystems to inspect their answers.
