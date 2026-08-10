# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Modal(Component):
    """A Modal component.
Modal with optional header. For more information, see: https://mantine.dev/core/modal/

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    Content.

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- centered (boolean; optional):
    Controls if modal should be centered.

- className (string; optional):
    Often used with CSS to style elements with common properties.

- classNames (dict; optional):
    add class names to Mantine components.

- closeButtonLabel (string; optional):
    Close button aria-label.

- closeOnClickOutside (boolean; optional):
    Should modal be closed when outside click was registered?.

- closeOnEscape (boolean; optional):
    Should modal be closed when escape is pressed?.

- fullScreen (boolean; optional):
    Determines whether the modal should take the entire screen.

- lockScroll (boolean; optional):
    Determines whether scroll should be locked when modal is opened,
    defaults to True.

- opened (boolean; default False):
    Mounts modal if True.

- overflow (a value equal to: 'outside', 'inside'; optional):
    Control vertical overflow behavior.

- overlayBlur (number; optional):
    Overlay blur in px.

- overlayColor (string; optional):
    Overlay color.

- overlayOpacity (number; optional):
    Overlay opacity.

- padding (number; optional):
    Modal padding from theme or number value for padding in px.

- radius (number; optional):
    Modal radius.

- shadow (boolean | number | string | dict | list; optional):
    Modal shadow from theme or css value.

- size (string | number; optional):
    Modal body width.

- style (boolean | number | string | dict | list; optional):
    Inline style.

- styles (boolean | number | string | dict | list; optional):
    Mantine styles API.

- sx (boolean | number | string | dict | list; optional):
    With sx you can add styles to component root element. If you need
    to customize styles of other elements within component use styles
    prop.

- title (a list of or a singular dash component, string or number; optional):
    Modal title, displayed in header before close button.

- transition (a value equal to: 'fade', 'skew-up', 'skew-down', 'rotate-right', 'rotate-left', 'slide-down', 'slide-up', 'slide-right', 'slide-left', 'scale-y', 'scale-x', 'scale', 'pop', 'pop-top-left', 'pop-top-right', 'pop-bottom-left', 'pop-bottom-right'; optional):
    Modal body transition.

- transitionDuration (number; optional):
    Duration in ms of modal transitions, set to 0 to disable all
    animations.

- transitionTimingFunction (string; optional):
    Modal body transitionTimingFunction, defaults to
    theme.transitionTimingFunction.

- trapFocus (boolean; optional):
    Disables focus trap.

- withCloseButton (boolean; optional):
    Hides close button if set to False, modal still can be closed with
    escape key and by clicking outside.

- withFocusReturn (boolean; optional):
    Determines whether focus should be returned to the last active
    element when drawer is closed.

- zIndex (number; optional):
    Modal z-index property."""
    _children_props = ['title']
    _base_nodes = ['title', 'children']
    _namespace = 'dash_mantine_components'
    _type = 'Modal'
    @_explicitize_args
    def __init__(self, children=None, opened=Component.UNDEFINED, title=Component.UNDEFINED, zIndex=Component.UNDEFINED, overflow=Component.UNDEFINED, withCloseButton=Component.UNDEFINED, overlayOpacity=Component.UNDEFINED, overlayColor=Component.UNDEFINED, overlayBlur=Component.UNDEFINED, fullScreen=Component.UNDEFINED, radius=Component.UNDEFINED, size=Component.UNDEFINED, transition=Component.UNDEFINED, transitionDuration=Component.UNDEFINED, transitionTimingFunction=Component.UNDEFINED, shadow=Component.UNDEFINED, padding=Component.UNDEFINED, closeOnClickOutside=Component.UNDEFINED, closeOnEscape=Component.UNDEFINED, trapFocus=Component.UNDEFINED, centered=Component.UNDEFINED, lockScroll=Component.UNDEFINED, withFocusReturn=Component.UNDEFINED, closeButtonLabel=Component.UNDEFINED, className=Component.UNDEFINED, classNames=Component.UNDEFINED, style=Component.UNDEFINED, styles=Component.UNDEFINED, id=Component.UNDEFINED, unstyled=Component.UNDEFINED, sx=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'centered', 'className', 'classNames', 'closeButtonLabel', 'closeOnClickOutside', 'closeOnEscape', 'fullScreen', 'lockScroll', 'opened', 'overflow', 'overlayBlur', 'overlayColor', 'overlayOpacity', 'padding', 'radius', 'shadow', 'size', 'style', 'styles', 'sx', 'title', 'transition', 'transitionDuration', 'transitionTimingFunction', 'trapFocus', 'unstyled', 'withCloseButton', 'withFocusReturn', 'zIndex']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'centered', 'className', 'classNames', 'closeButtonLabel', 'closeOnClickOutside', 'closeOnEscape', 'fullScreen', 'lockScroll', 'opened', 'overflow', 'overlayBlur', 'overlayColor', 'overlayOpacity', 'padding', 'radius', 'shadow', 'size', 'style', 'styles', 'sx', 'title', 'transition', 'transitionDuration', 'transitionTimingFunction', 'trapFocus', 'unstyled', 'withCloseButton', 'withFocusReturn', 'zIndex']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Modal, self).__init__(children=children, **args)
