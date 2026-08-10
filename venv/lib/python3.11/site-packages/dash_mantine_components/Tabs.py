# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Tabs(Component):
    """A Tabs component.
Switch between different views. For more information, see: https://mantine.dev/core/tabs/

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    Tabs content.

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- activateTabWithKeyboard (boolean; optional):
    Determines whether tab should be activated with arrow key press,
    defaults to True.

- allowTabDeactivation (boolean; optional):
    Determines whether tab can be deactivated, defaults to False.

- className (string; optional):
    Often used with CSS to style elements with common properties.

- classNames (dict; optional):
    add class names to Mantine components.

- color (boolean | number | string | dict | list; optional):
    Key of theme.colors.

- inverted (boolean; optional):
    Determines whether tabs should have inverted styles.

- keepMounted (boolean; optional):
    If set to False, Tabs.Panel content will not stay mounted when tab
    is not active.

- loop (boolean; optional):
    Determines whether arrow key presses should loop though items
    (first to last and last to first).

- orientation (a value equal to: 'horizontal', 'vertical'; optional):
    Tabs orientation, vertical or horizontal.

- persisted_props (list of strings; default ["value"]):
    Properties whose user interactions will persist after refreshing
    the component or the page. Since only `value` is allowed this prop
    can normally be ignored.

- persistence (string | number; optional):
    Used to allow user interactions in this component to be persisted
    when the component - or the page - is refreshed. If `persisted` is
    truthy and hasn't changed from its previous value, a `value` that
    the user has changed while using the app will keep that change, as
    long as the new `value` also matches what was given originally.
    Used in conjunction with `persistence_type`.

- persistence_type (a value equal to: 'local', 'session', 'memory'; default 'local'):
    Where persisted user changes will be stored: memory: only kept in
    memory, reset on page refresh. local: window.localStorage, data is
    kept after the browser quit. session: window.sessionStorage, data
    is cleared once the browser quit.

- placement (a value equal to: 'left', 'right'; optional):
    Tabs.List placement relative to Tabs.Panel, applicable only for
    orientation=\"vertical\", left by default.

- radius (number; optional):
    Tabs border-radius from theme.radius or number ti set value from
    theme, defaults to theme.defaultRadius.

- style (boolean | number | string | dict | list; optional):
    Inline style.

- styles (boolean | number | string | dict | list; optional):
    Mantine styles API.

- sx (boolean | number | string | dict | list; optional):
    With sx you can add styles to component root element. If you need
    to customize styles of other elements within component use styles
    prop.

- value (string; optional):
    Value for controlled component.

- variant (a value equal to: 'default', 'outline', 'pills'; optional):
    Controls component visuals."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_mantine_components'
    _type = 'Tabs'
    @_explicitize_args
    def __init__(self, children=None, value=Component.UNDEFINED, orientation=Component.UNDEFINED, loop=Component.UNDEFINED, activateTabWithKeyboard=Component.UNDEFINED, allowTabDeactivation=Component.UNDEFINED, variant=Component.UNDEFINED, color=Component.UNDEFINED, radius=Component.UNDEFINED, inverted=Component.UNDEFINED, keepMounted=Component.UNDEFINED, placement=Component.UNDEFINED, persistence=Component.UNDEFINED, persisted_props=Component.UNDEFINED, persistence_type=Component.UNDEFINED, className=Component.UNDEFINED, classNames=Component.UNDEFINED, style=Component.UNDEFINED, styles=Component.UNDEFINED, id=Component.UNDEFINED, unstyled=Component.UNDEFINED, sx=Component.UNDEFINED, m=Component.UNDEFINED, my=Component.UNDEFINED, mx=Component.UNDEFINED, mt=Component.UNDEFINED, mb=Component.UNDEFINED, ml=Component.UNDEFINED, mr=Component.UNDEFINED, p=Component.UNDEFINED, py=Component.UNDEFINED, px=Component.UNDEFINED, pt=Component.UNDEFINED, pb=Component.UNDEFINED, pl=Component.UNDEFINED, pr=Component.UNDEFINED, bg=Component.UNDEFINED, c=Component.UNDEFINED, opacity=Component.UNDEFINED, ff=Component.UNDEFINED, fz=Component.UNDEFINED, fw=Component.UNDEFINED, lts=Component.UNDEFINED, ta=Component.UNDEFINED, lh=Component.UNDEFINED, fs=Component.UNDEFINED, tt=Component.UNDEFINED, td=Component.UNDEFINED, w=Component.UNDEFINED, miw=Component.UNDEFINED, maw=Component.UNDEFINED, h=Component.UNDEFINED, mih=Component.UNDEFINED, mah=Component.UNDEFINED, bgsz=Component.UNDEFINED, bgp=Component.UNDEFINED, bgr=Component.UNDEFINED, pos=Component.UNDEFINED, top=Component.UNDEFINED, left=Component.UNDEFINED, bottom=Component.UNDEFINED, right=Component.UNDEFINED, inset=Component.UNDEFINED, display=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'activateTabWithKeyboard', 'allowTabDeactivation', 'bg', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'color', 'display', 'ff', 'fs', 'fw', 'fz', 'h', 'inset', 'inverted', 'keepMounted', 'left', 'lh', 'loop', 'lts', 'm', 'mah', 'maw', 'mb', 'mih', 'miw', 'ml', 'mr', 'mt', 'mx', 'my', 'opacity', 'orientation', 'p', 'pb', 'persisted_props', 'persistence', 'persistence_type', 'pl', 'placement', 'pos', 'pr', 'pt', 'px', 'py', 'radius', 'right', 'style', 'styles', 'sx', 'ta', 'td', 'top', 'tt', 'unstyled', 'value', 'variant', 'w']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'activateTabWithKeyboard', 'allowTabDeactivation', 'bg', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'color', 'display', 'ff', 'fs', 'fw', 'fz', 'h', 'inset', 'inverted', 'keepMounted', 'left', 'lh', 'loop', 'lts', 'm', 'mah', 'maw', 'mb', 'mih', 'miw', 'ml', 'mr', 'mt', 'mx', 'my', 'opacity', 'orientation', 'p', 'pb', 'persisted_props', 'persistence', 'persistence_type', 'pl', 'placement', 'pos', 'pr', 'pt', 'px', 'py', 'radius', 'right', 'style', 'styles', 'sx', 'ta', 'td', 'top', 'tt', 'unstyled', 'value', 'variant', 'w']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Tabs, self).__init__(children=children, **args)
