# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class HoverCard(Component):
    """A HoverCard component.
Display popover section when target element is hovered. For more information, see: https://mantine.dev/core/hover-card/

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    HoverCard content.

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- arrowOffset (number; optional):
    Arrow offset in px.

- arrowRadius (number; optional):
    Arrow radius in px.

- arrowSize (number; optional):
    Arrow size in px.

- className (string; optional):
    Often used with CSS to style elements with common properties.

- classNames (dict; optional):
    add class names to Mantine components.

- closeDelay (number; optional):
    Close delay in ms.

- disabled (boolean; optional):
    Radius from theme.radius or number to set border-radius in px.

- exitTransitionDuration (number; optional):
    Exit transition duration in ms.

- middlewares (dict; optional):
    Floating ui middlewares to configure position handling.

    `middlewares` is a dict with keys:

    - flip (boolean; required)

    - inline (boolean; optional)

    - shift (boolean; required)

- offset (number; optional):
    Space between target element and dropdown in px.

- openDelay (number; optional):
    Open delay in ms.

- position (a value equal to: 'top', 'right', 'bottom', 'left', 'top-end', 'top-start', 'right-end', 'right-start', 'bottom-end', 'bottom-start', 'left-end', 'left-start'; optional):
    Dropdown position relative to target.

- radius (number; optional):
    Radius from theme.radius or number to set border-radius in px.

- returnFocus (boolean; optional):
    Determines whether focus should be automatically returned to
    control when dropdown closes, False by default.

- shadow (boolean | number | string | dict | list; optional):
    Key of theme.shadow or any other valid css box-shadow value.

- style (boolean | number | string | dict | list; optional):
    Inline style.

- styles (boolean | number | string | dict | list; optional):
    Mantine styles API.

- sx (boolean | number | string | dict | list; optional):
    With sx you can add styles to component root element. If you need
    to customize styles of other elements within component use styles
    prop.

- transition (a value equal to: 'fade', 'skew-up', 'skew-down', 'rotate-right', 'rotate-left', 'slide-down', 'slide-up', 'slide-right', 'slide-left', 'scale-y', 'scale-x', 'scale', 'pop', 'pop-top-left', 'pop-top-right', 'pop-bottom-left', 'pop-bottom-right'; optional):
    One of premade transitions ot transition object.

- transitionDuration (number; optional):
    Transition duration in ms.

- width (string | number; optional):
    Dropdown width, or 'target' to make dropdown width the same as
    target element.

- withArrow (boolean; optional):
    Determines whether component should have an arrow.

- withinPortal (boolean; optional):
    Determines whether dropdown should be rendered within Portal,
    defaults to False.

- zIndex (number; optional):
    Dropdown z-index."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_mantine_components'
    _type = 'HoverCard'
    @_explicitize_args
    def __init__(self, children=None, openDelay=Component.UNDEFINED, closeDelay=Component.UNDEFINED, position=Component.UNDEFINED, offset=Component.UNDEFINED, transition=Component.UNDEFINED, transitionDuration=Component.UNDEFINED, exitTransitionDuration=Component.UNDEFINED, width=Component.UNDEFINED, withArrow=Component.UNDEFINED, arrowSize=Component.UNDEFINED, arrowOffset=Component.UNDEFINED, arrowRadius=Component.UNDEFINED, withinPortal=Component.UNDEFINED, disabled=Component.UNDEFINED, returnFocus=Component.UNDEFINED, zIndex=Component.UNDEFINED, radius=Component.UNDEFINED, shadow=Component.UNDEFINED, middlewares=Component.UNDEFINED, className=Component.UNDEFINED, classNames=Component.UNDEFINED, style=Component.UNDEFINED, styles=Component.UNDEFINED, id=Component.UNDEFINED, unstyled=Component.UNDEFINED, sx=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'arrowOffset', 'arrowRadius', 'arrowSize', 'className', 'classNames', 'closeDelay', 'disabled', 'exitTransitionDuration', 'middlewares', 'offset', 'openDelay', 'position', 'radius', 'returnFocus', 'shadow', 'style', 'styles', 'sx', 'transition', 'transitionDuration', 'unstyled', 'width', 'withArrow', 'withinPortal', 'zIndex']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'arrowOffset', 'arrowRadius', 'arrowSize', 'className', 'classNames', 'closeDelay', 'disabled', 'exitTransitionDuration', 'middlewares', 'offset', 'openDelay', 'position', 'radius', 'returnFocus', 'shadow', 'style', 'styles', 'sx', 'transition', 'transitionDuration', 'unstyled', 'width', 'withArrow', 'withinPortal', 'zIndex']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(HoverCard, self).__init__(children=children, **args)
