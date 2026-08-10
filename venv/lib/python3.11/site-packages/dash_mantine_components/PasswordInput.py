# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class PasswordInput(Component):
    """A PasswordInput component.
Capture password from user with option to toggle visibility. For more information, see: https://mantine.dev/core/password-input/

Keyword arguments:

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- className (string; optional):
    Often used with CSS to style elements with common properties.

- classNames (dict; optional):
    add class names to Mantine components.

- debounce (number; default 0):
    Debounce time.

- description (a list of or a singular dash component, string or number; optional):
    Input description, displayed after label.

- disabled (boolean; optional):
    Disabled input state.

- error (a list of or a singular dash component, string or number; optional):
    Displays error message after input.

- icon (a list of or a singular dash component, string or number; optional):
    Adds icon on the left side of input.

- iconWidth (number; optional):
    Width of icon section in px.

- inputWrapperOrder (list of a value equal to: 'label', 'description', 'error', 'input's; optional):
    Controls order of the Input.Wrapper elements.

- label (a list of or a singular dash component, string or number; optional):
    Input label, displayed before input.

- name (string; optional):
    Name prop.

- placeholder (string; optional):
    Placeholder.

- radius (number; optional):
    Input border-radius from theme or number to set border-radius in
    px.

- required (boolean; optional):
    Sets required on input element   Adds required attribute to the
    input and red asterisk on the right side of label.

- rightSection (a list of or a singular dash component, string or number; optional):
    Right section of input, similar to icon but on the right.

- rightSectionWidth (number; optional):
    Width of right section, is used to calculate input padding-right.

- size (a value equal to: 'xs', 'sm', 'md', 'lg', 'xl'; optional):
    Input size.

- style (boolean | number | string | dict | list; optional):
    Inline style.

- styles (boolean | number | string | dict | list; optional):
    Mantine styles API.

- sx (boolean | number | string | dict | list; optional):
    With sx you can add styles to component root element. If you need
    to customize styles of other elements within component use styles
    prop.

- toggleTabIndex (a value equal to: 0, -1; optional):
    Toggle button tabIndex, set to 0 to make button focusable with tab
    key.

- value (string; default ''):
    Value for controlled input.

- variant (a value equal to: 'default', 'filled', 'unstyled'; optional):
    Defines input appearance, defaults to default in light color
    scheme and filled in dark.

- visible (boolean; optional):
    Determines whether input content should be visible (controlled).

- withAsterisk (boolean; optional):
    Determines whether required asterisk should be rendered, overrides
    required prop, does not add required attribute to the input."""
    _children_props = ['icon', 'rightSection', 'label', 'description', 'error']
    _base_nodes = ['icon', 'rightSection', 'label', 'description', 'error', 'children']
    _namespace = 'dash_mantine_components'
    _type = 'PasswordInput'
    @_explicitize_args
    def __init__(self, toggleTabIndex=Component.UNDEFINED, visible=Component.UNDEFINED, value=Component.UNDEFINED, icon=Component.UNDEFINED, iconWidth=Component.UNDEFINED, rightSection=Component.UNDEFINED, rightSectionWidth=Component.UNDEFINED, required=Component.UNDEFINED, radius=Component.UNDEFINED, variant=Component.UNDEFINED, disabled=Component.UNDEFINED, size=Component.UNDEFINED, placeholder=Component.UNDEFINED, name=Component.UNDEFINED, debounce=Component.UNDEFINED, label=Component.UNDEFINED, description=Component.UNDEFINED, error=Component.UNDEFINED, withAsterisk=Component.UNDEFINED, inputWrapperOrder=Component.UNDEFINED, className=Component.UNDEFINED, classNames=Component.UNDEFINED, style=Component.UNDEFINED, styles=Component.UNDEFINED, id=Component.UNDEFINED, unstyled=Component.UNDEFINED, sx=Component.UNDEFINED, m=Component.UNDEFINED, my=Component.UNDEFINED, mx=Component.UNDEFINED, mt=Component.UNDEFINED, mb=Component.UNDEFINED, ml=Component.UNDEFINED, mr=Component.UNDEFINED, p=Component.UNDEFINED, py=Component.UNDEFINED, px=Component.UNDEFINED, pt=Component.UNDEFINED, pb=Component.UNDEFINED, pl=Component.UNDEFINED, pr=Component.UNDEFINED, bg=Component.UNDEFINED, c=Component.UNDEFINED, opacity=Component.UNDEFINED, ff=Component.UNDEFINED, fz=Component.UNDEFINED, fw=Component.UNDEFINED, lts=Component.UNDEFINED, ta=Component.UNDEFINED, lh=Component.UNDEFINED, fs=Component.UNDEFINED, tt=Component.UNDEFINED, td=Component.UNDEFINED, w=Component.UNDEFINED, miw=Component.UNDEFINED, maw=Component.UNDEFINED, h=Component.UNDEFINED, mih=Component.UNDEFINED, mah=Component.UNDEFINED, bgsz=Component.UNDEFINED, bgp=Component.UNDEFINED, bgr=Component.UNDEFINED, pos=Component.UNDEFINED, top=Component.UNDEFINED, left=Component.UNDEFINED, bottom=Component.UNDEFINED, right=Component.UNDEFINED, inset=Component.UNDEFINED, display=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'bg', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'debounce', 'description', 'disabled', 'display', 'error', 'ff', 'fs', 'fw', 'fz', 'h', 'icon', 'iconWidth', 'inputWrapperOrder', 'inset', 'label', 'left', 'lh', 'lts', 'm', 'mah', 'maw', 'mb', 'mih', 'miw', 'ml', 'mr', 'mt', 'mx', 'my', 'name', 'opacity', 'p', 'pb', 'pl', 'placeholder', 'pos', 'pr', 'pt', 'px', 'py', 'radius', 'required', 'right', 'rightSection', 'rightSectionWidth', 'size', 'style', 'styles', 'sx', 'ta', 'td', 'toggleTabIndex', 'top', 'tt', 'unstyled', 'value', 'variant', 'visible', 'w', 'withAsterisk']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'bg', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'debounce', 'description', 'disabled', 'display', 'error', 'ff', 'fs', 'fw', 'fz', 'h', 'icon', 'iconWidth', 'inputWrapperOrder', 'inset', 'label', 'left', 'lh', 'lts', 'm', 'mah', 'maw', 'mb', 'mih', 'miw', 'ml', 'mr', 'mt', 'mx', 'my', 'name', 'opacity', 'p', 'pb', 'pl', 'placeholder', 'pos', 'pr', 'pt', 'px', 'py', 'radius', 'required', 'right', 'rightSection', 'rightSectionWidth', 'size', 'style', 'styles', 'sx', 'ta', 'td', 'toggleTabIndex', 'top', 'tt', 'unstyled', 'value', 'variant', 'visible', 'w', 'withAsterisk']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(PasswordInput, self).__init__(**args)
