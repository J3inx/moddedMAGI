# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class List(Component):
    """A List component.
Display ordered or unordered list, see: https://mantine.dev/core/list/

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    dmc.ListItem components only.

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- center (boolean; optional):
    Center items with icon.

- className (string; optional):
    Often used with CSS to style elements with common properties.

- classNames (dict; optional):
    add class names to Mantine components.

- icon (a list of or a singular dash component, string or number; optional):
    Icon that should replace list item dot.

- listStyleType (a value equal to: 'disc', 'circle', 'square', 'decimal', 'lower-roman', 'upper-roman', 'lower-greek', 'lower-latin', 'upper-latin', 'lower-alpha', 'upper-alpha', 'none', 'inherit'; optional):
    List style.

- size (number; optional):
    Font size from theme or number to set value in px.

- spacing (number; optional):
    Spacing between items from theme or number to set value in px.

- style (boolean | number | string | dict | list; optional):
    Inline style.

- styles (boolean | number | string | dict | list; optional):
    Mantine styles API.

- sx (boolean | number | string | dict | list; optional):
    With sx you can add styles to component root element. If you need
    to customize styles of other elements within component use styles
    prop.

- type (a value equal to: 'ordered', 'unordered'; optional):
    List type: ol or ul.

- withPadding (boolean; optional):
    Include padding-left to offset list from main content."""
    _children_props = ['icon']
    _base_nodes = ['icon', 'children']
    _namespace = 'dash_mantine_components'
    _type = 'List'
    @_explicitize_args
    def __init__(self, children=None, type=Component.UNDEFINED, withPadding=Component.UNDEFINED, size=Component.UNDEFINED, icon=Component.UNDEFINED, spacing=Component.UNDEFINED, center=Component.UNDEFINED, listStyleType=Component.UNDEFINED, className=Component.UNDEFINED, classNames=Component.UNDEFINED, style=Component.UNDEFINED, styles=Component.UNDEFINED, id=Component.UNDEFINED, unstyled=Component.UNDEFINED, sx=Component.UNDEFINED, m=Component.UNDEFINED, my=Component.UNDEFINED, mx=Component.UNDEFINED, mt=Component.UNDEFINED, mb=Component.UNDEFINED, ml=Component.UNDEFINED, mr=Component.UNDEFINED, p=Component.UNDEFINED, py=Component.UNDEFINED, px=Component.UNDEFINED, pt=Component.UNDEFINED, pb=Component.UNDEFINED, pl=Component.UNDEFINED, pr=Component.UNDEFINED, bg=Component.UNDEFINED, c=Component.UNDEFINED, opacity=Component.UNDEFINED, ff=Component.UNDEFINED, fz=Component.UNDEFINED, fw=Component.UNDEFINED, lts=Component.UNDEFINED, ta=Component.UNDEFINED, lh=Component.UNDEFINED, fs=Component.UNDEFINED, tt=Component.UNDEFINED, td=Component.UNDEFINED, w=Component.UNDEFINED, miw=Component.UNDEFINED, maw=Component.UNDEFINED, h=Component.UNDEFINED, mih=Component.UNDEFINED, mah=Component.UNDEFINED, bgsz=Component.UNDEFINED, bgp=Component.UNDEFINED, bgr=Component.UNDEFINED, pos=Component.UNDEFINED, top=Component.UNDEFINED, left=Component.UNDEFINED, bottom=Component.UNDEFINED, right=Component.UNDEFINED, inset=Component.UNDEFINED, display=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'bg', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'center', 'className', 'classNames', 'display', 'ff', 'fs', 'fw', 'fz', 'h', 'icon', 'inset', 'left', 'lh', 'listStyleType', 'lts', 'm', 'mah', 'maw', 'mb', 'mih', 'miw', 'ml', 'mr', 'mt', 'mx', 'my', 'opacity', 'p', 'pb', 'pl', 'pos', 'pr', 'pt', 'px', 'py', 'right', 'size', 'spacing', 'style', 'styles', 'sx', 'ta', 'td', 'top', 'tt', 'type', 'unstyled', 'w', 'withPadding']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'bg', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'center', 'className', 'classNames', 'display', 'ff', 'fs', 'fw', 'fz', 'h', 'icon', 'inset', 'left', 'lh', 'listStyleType', 'lts', 'm', 'mah', 'maw', 'mb', 'mih', 'miw', 'ml', 'mr', 'mt', 'mx', 'my', 'opacity', 'p', 'pb', 'pl', 'pos', 'pr', 'pt', 'px', 'py', 'right', 'size', 'spacing', 'style', 'styles', 'sx', 'ta', 'td', 'top', 'tt', 'type', 'unstyled', 'w', 'withPadding']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(List, self).__init__(children=children, **args)
