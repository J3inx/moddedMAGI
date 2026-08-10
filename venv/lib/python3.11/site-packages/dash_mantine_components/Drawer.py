# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Drawer(Component):
    """A Drawer component.
Display overlay area at any side of the screen. For more information, see: https://mantine.dev/core/drawer/

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    Drawer Content *.

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- className (string; optional):
    Often used with CSS to style elements with common properties.

- classNames (dict; optional):
    add class names to Mantine components.

- closeOnClickOutside (boolean; optional):
    Disable onMouseDown trigger for outside events.

- closeOnEscape (boolean; optional):
    Disable onKeyDownCapture trigger for escape key press.

- lockScroll (boolean; optional):
    Disables scroll lock.

- opened (boolean; default False):
    If True drawer is mounted to the dom.

- overlayBlur (number; optional):
    Overlay blur in px.

- overlayColor (string; optional):
    Overlay color, for example, #000.

- overlayOpacity (number; optional):
    Overlay opacity, number from 0 to 1.

- padding (number; optional):
    Drawer body padding from theme or number for padding in px.

- position (a value equal to: 'left', 'right', 'top', 'bottom'; optional):
    Drawer body position.

- shadow (boolean | number | string | dict | list; optional):
    Drawer body shadow from theme or any css shadow value.

- size (string | number; optional):
    Drawer body width (right | left position) or height (top | bottom
    position), cannot exceed 100vh for height and 100% for width.

- style (boolean | number | string | dict | list; optional):
    Inline style.

- styles (boolean | number | string | dict | list; optional):
    Mantine styles API.

- sx (boolean | number | string | dict | list; optional):
    With sx you can add styles to component root element. If you need
    to customize styles of other elements within component use styles
    prop.

- title (a list of or a singular dash component, string or number; optional):
    Drawer title, displayed in header before close button.

- transition (a value equal to: 'fade', 'skew-up', 'skew-down', 'rotate-right', 'rotate-left', 'slide-down', 'slide-up', 'slide-right', 'slide-left', 'scale-y', 'scale-x', 'scale', 'pop', 'pop-top-left', 'pop-top-right', 'pop-bottom-left', 'pop-bottom-right'; optional):
    Drawer appear and disappear transition, see Transition component
    for full documentation.

- transitionDuration (number; optional):
    Transition duration in ms.

- transitionTimingFunction (string; optional):
    Drawer transitionTimingFunction css property.

- trapFocus (boolean; optional):
    Disables focus trap.

- withCloseButton (boolean; optional):
    Hides close button if set to False, drawer still can be closed
    with escape key and by clicking outside.

- withFocusReturn (boolean; optional):
    Determines whether focus should be returned to the last active
    element when drawer is closed.

- withOverlay (boolean; optional):
    Removes overlay entirely.

- zIndex (number; optional):
    Drawer z-index property."""
    _children_props = ['title']
    _base_nodes = ['title', 'children']
    _namespace = 'dash_mantine_components'
    _type = 'Drawer'
    @_explicitize_args
    def __init__(self, children=None, opened=Component.UNDEFINED, position=Component.UNDEFINED, size=Component.UNDEFINED, shadow=Component.UNDEFINED, padding=Component.UNDEFINED, zIndex=Component.UNDEFINED, trapFocus=Component.UNDEFINED, lockScroll=Component.UNDEFINED, closeOnClickOutside=Component.UNDEFINED, closeOnEscape=Component.UNDEFINED, transition=Component.UNDEFINED, transitionDuration=Component.UNDEFINED, transitionTimingFunction=Component.UNDEFINED, withOverlay=Component.UNDEFINED, overlayOpacity=Component.UNDEFINED, overlayColor=Component.UNDEFINED, overlayBlur=Component.UNDEFINED, title=Component.UNDEFINED, withCloseButton=Component.UNDEFINED, withFocusReturn=Component.UNDEFINED, className=Component.UNDEFINED, classNames=Component.UNDEFINED, style=Component.UNDEFINED, styles=Component.UNDEFINED, id=Component.UNDEFINED, unstyled=Component.UNDEFINED, sx=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'className', 'classNames', 'closeOnClickOutside', 'closeOnEscape', 'lockScroll', 'opened', 'overlayBlur', 'overlayColor', 'overlayOpacity', 'padding', 'position', 'shadow', 'size', 'style', 'styles', 'sx', 'title', 'transition', 'transitionDuration', 'transitionTimingFunction', 'trapFocus', 'unstyled', 'withCloseButton', 'withFocusReturn', 'withOverlay', 'zIndex']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'classNames', 'closeOnClickOutside', 'closeOnEscape', 'lockScroll', 'opened', 'overlayBlur', 'overlayColor', 'overlayOpacity', 'padding', 'position', 'shadow', 'size', 'style', 'styles', 'sx', 'title', 'transition', 'transitionDuration', 'transitionTimingFunction', 'trapFocus', 'unstyled', 'withCloseButton', 'withFocusReturn', 'withOverlay', 'zIndex']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Drawer, self).__init__(children=children, **args)
