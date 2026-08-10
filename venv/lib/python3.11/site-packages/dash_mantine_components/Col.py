# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Col(Component):
    """A Col component.
Inline or block code without syntax highlight. For more information, see: https://mantine.dev/core/code/

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    Col content.

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- className (string; optional):
    Often used with CSS to style elements with common properties.

- classNames (dict; optional):
    add class names to Mantine components.

- lg (number; optional):
    Col span at (min-width: theme.breakpoints.lg).

- md (number; optional):
    Col span at (min-width: theme.breakpoints.md).

- offset (number; optional):
    Column left offset.

- offsetLg (number; optional):
    Column left offset at (min-width: theme.breakpoints.lg).

- offsetMd (number; optional):
    Column left offset at (min-width: theme.breakpoints.md).

- offsetSm (number; optional):
    Column left offset at (min-width: theme.breakpoints.sm).

- offsetXl (number; optional):
    Column left offset at (min-width: theme.breakpoints.xl).

- offsetXs (number; optional):
    Column left offset at (min-width: theme.breakpoints.xs).

- order (number; optional):
    Default col order.

- orderLg (number; optional):
    Col order at (min-width: theme.breakpoints.lg).

- orderMd (number; optional):
    Col order at (min-width: theme.breakpoints.md).

- orderSm (number; optional):
    Col order at (min-width: theme.breakpoints.sm).

- orderXl (number; optional):
    Col order at (min-width: theme.breakpoints.xl).

- orderXs (number; optional):
    Col order at (min-width: theme.breakpoints.xs).

- sm (number; optional):
    Col span at (min-width: theme.breakpoints.sm).

- span (number; optional):
    Default col span.

- style (boolean | number | string | dict | list; optional):
    Inline style.

- styles (boolean | number | string | dict | list; optional):
    Mantine styles API.

- sx (boolean | number | string | dict | list; optional):
    With sx you can add styles to component root element. If you need
    to customize styles of other elements within component use styles
    prop.

- xl (number; optional):
    Col span at (min-width: theme.breakpoints.xl).

- xs (number; optional):
    Col span at (min-width: theme.breakpoints.xs)."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_mantine_components'
    _type = 'Col'
    @_explicitize_args
    def __init__(self, children=None, span=Component.UNDEFINED, offset=Component.UNDEFINED, order=Component.UNDEFINED, orderXs=Component.UNDEFINED, orderSm=Component.UNDEFINED, orderMd=Component.UNDEFINED, orderLg=Component.UNDEFINED, orderXl=Component.UNDEFINED, offsetXs=Component.UNDEFINED, offsetSm=Component.UNDEFINED, offsetMd=Component.UNDEFINED, offsetLg=Component.UNDEFINED, offsetXl=Component.UNDEFINED, xs=Component.UNDEFINED, sm=Component.UNDEFINED, md=Component.UNDEFINED, lg=Component.UNDEFINED, xl=Component.UNDEFINED, className=Component.UNDEFINED, classNames=Component.UNDEFINED, style=Component.UNDEFINED, styles=Component.UNDEFINED, id=Component.UNDEFINED, unstyled=Component.UNDEFINED, sx=Component.UNDEFINED, m=Component.UNDEFINED, my=Component.UNDEFINED, mx=Component.UNDEFINED, mt=Component.UNDEFINED, mb=Component.UNDEFINED, ml=Component.UNDEFINED, mr=Component.UNDEFINED, p=Component.UNDEFINED, py=Component.UNDEFINED, px=Component.UNDEFINED, pt=Component.UNDEFINED, pb=Component.UNDEFINED, pl=Component.UNDEFINED, pr=Component.UNDEFINED, bg=Component.UNDEFINED, c=Component.UNDEFINED, opacity=Component.UNDEFINED, ff=Component.UNDEFINED, fz=Component.UNDEFINED, fw=Component.UNDEFINED, lts=Component.UNDEFINED, ta=Component.UNDEFINED, lh=Component.UNDEFINED, fs=Component.UNDEFINED, tt=Component.UNDEFINED, td=Component.UNDEFINED, w=Component.UNDEFINED, miw=Component.UNDEFINED, maw=Component.UNDEFINED, h=Component.UNDEFINED, mih=Component.UNDEFINED, mah=Component.UNDEFINED, bgsz=Component.UNDEFINED, bgp=Component.UNDEFINED, bgr=Component.UNDEFINED, pos=Component.UNDEFINED, top=Component.UNDEFINED, left=Component.UNDEFINED, bottom=Component.UNDEFINED, right=Component.UNDEFINED, inset=Component.UNDEFINED, display=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'bg', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'display', 'ff', 'fs', 'fw', 'fz', 'h', 'inset', 'left', 'lg', 'lh', 'lts', 'm', 'mah', 'maw', 'mb', 'md', 'mih', 'miw', 'ml', 'mr', 'mt', 'mx', 'my', 'offset', 'offsetLg', 'offsetMd', 'offsetSm', 'offsetXl', 'offsetXs', 'opacity', 'order', 'orderLg', 'orderMd', 'orderSm', 'orderXl', 'orderXs', 'p', 'pb', 'pl', 'pos', 'pr', 'pt', 'px', 'py', 'right', 'sm', 'span', 'style', 'styles', 'sx', 'ta', 'td', 'top', 'tt', 'unstyled', 'w', 'xl', 'xs']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'bg', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'display', 'ff', 'fs', 'fw', 'fz', 'h', 'inset', 'left', 'lg', 'lh', 'lts', 'm', 'mah', 'maw', 'mb', 'md', 'mih', 'miw', 'ml', 'mr', 'mt', 'mx', 'my', 'offset', 'offsetLg', 'offsetMd', 'offsetSm', 'offsetXl', 'offsetXs', 'opacity', 'order', 'orderLg', 'orderMd', 'orderSm', 'orderXl', 'orderXs', 'p', 'pb', 'pl', 'pos', 'pr', 'pt', 'px', 'py', 'right', 'sm', 'span', 'style', 'styles', 'sx', 'ta', 'td', 'top', 'tt', 'unstyled', 'w', 'xl', 'xs']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Col, self).__init__(children=children, **args)
