# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class ActionIcon(Component):
    """An ActionIcon component.
Icon button. For more information, see: https://mantine.dev/core/action-icon/

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    Icon.

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- className (string; optional):
    Often used with CSS to style elements with common properties.

- classNames (dict; optional):
    add class names to Mantine components.

- color (boolean | number | string | dict | list; optional):
    Key of theme.colors.

- disabled (boolean; optional):
    Indicates disabled state.

- gradient (dict; optional):
    Controls gradient settings in gradient variant only.

    `gradient` is a dict with keys:

    - deg (number; optional)

    - from (string; required)

    - to (string; required)

- loaderProps (dict; optional):
    Props spread to Loader component.

    `loaderProps` is a dict with keys:

    - color (boolean | number | string | dict | list; optional):
        Loader color from theme.

    - size (number; optional):
        Defines width of loader.

    - variant (a value equal to: 'bars', 'oval', 'dots'; optional):
        Loader appearance.

- loading (boolean; optional):
    Indicates loading state.

- n_clicks (number; default 0):
    An integer that represents the number of times that this element
    has been clicked on.

- radius (number; optional):
    Button border-radius from theme or number to set border-radius in
    px.

- size (number; optional):
    Predefined icon size or number to set width and height in px.

- style (boolean | number | string | dict | list; optional):
    Inline style.

- styles (boolean | number | string | dict | list; optional):
    Mantine styles API.

- sx (boolean | number | string | dict | list; optional):
    With sx you can add styles to component root element. If you need
    to customize styles of other elements within component use styles
    prop.

- title (string; optional):
    Set title prop to make ActionIcon visible to screen readers.

- variant (a value equal to: 'subtle', 'filled', 'outline', 'light', 'default', 'transparent', 'gradient'; optional):
    Controls appearance."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_mantine_components'
    _type = 'ActionIcon'
    @_explicitize_args
    def __init__(self, children=None, variant=Component.UNDEFINED, color=Component.UNDEFINED, gradient=Component.UNDEFINED, radius=Component.UNDEFINED, size=Component.UNDEFINED, loaderProps=Component.UNDEFINED, loading=Component.UNDEFINED, disabled=Component.UNDEFINED, n_clicks=Component.UNDEFINED, title=Component.UNDEFINED, className=Component.UNDEFINED, classNames=Component.UNDEFINED, style=Component.UNDEFINED, styles=Component.UNDEFINED, id=Component.UNDEFINED, unstyled=Component.UNDEFINED, sx=Component.UNDEFINED, m=Component.UNDEFINED, my=Component.UNDEFINED, mx=Component.UNDEFINED, mt=Component.UNDEFINED, mb=Component.UNDEFINED, ml=Component.UNDEFINED, mr=Component.UNDEFINED, p=Component.UNDEFINED, py=Component.UNDEFINED, px=Component.UNDEFINED, pt=Component.UNDEFINED, pb=Component.UNDEFINED, pl=Component.UNDEFINED, pr=Component.UNDEFINED, bg=Component.UNDEFINED, c=Component.UNDEFINED, opacity=Component.UNDEFINED, ff=Component.UNDEFINED, fz=Component.UNDEFINED, fw=Component.UNDEFINED, lts=Component.UNDEFINED, ta=Component.UNDEFINED, lh=Component.UNDEFINED, fs=Component.UNDEFINED, tt=Component.UNDEFINED, td=Component.UNDEFINED, w=Component.UNDEFINED, miw=Component.UNDEFINED, maw=Component.UNDEFINED, h=Component.UNDEFINED, mih=Component.UNDEFINED, mah=Component.UNDEFINED, bgsz=Component.UNDEFINED, bgp=Component.UNDEFINED, bgr=Component.UNDEFINED, pos=Component.UNDEFINED, top=Component.UNDEFINED, left=Component.UNDEFINED, bottom=Component.UNDEFINED, right=Component.UNDEFINED, inset=Component.UNDEFINED, display=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'bg', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'color', 'disabled', 'display', 'ff', 'fs', 'fw', 'fz', 'gradient', 'h', 'inset', 'left', 'lh', 'loaderProps', 'loading', 'lts', 'm', 'mah', 'maw', 'mb', 'mih', 'miw', 'ml', 'mr', 'mt', 'mx', 'my', 'n_clicks', 'opacity', 'p', 'pb', 'pl', 'pos', 'pr', 'pt', 'px', 'py', 'radius', 'right', 'size', 'style', 'styles', 'sx', 'ta', 'td', 'title', 'top', 'tt', 'unstyled', 'variant', 'w']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'bg', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'color', 'disabled', 'display', 'ff', 'fs', 'fw', 'fz', 'gradient', 'h', 'inset', 'left', 'lh', 'loaderProps', 'loading', 'lts', 'm', 'mah', 'maw', 'mb', 'mih', 'miw', 'ml', 'mr', 'mt', 'mx', 'my', 'n_clicks', 'opacity', 'p', 'pb', 'pl', 'pos', 'pr', 'pt', 'px', 'py', 'radius', 'right', 'size', 'style', 'styles', 'sx', 'ta', 'td', 'title', 'top', 'tt', 'unstyled', 'variant', 'w']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(ActionIcon, self).__init__(children=children, **args)
