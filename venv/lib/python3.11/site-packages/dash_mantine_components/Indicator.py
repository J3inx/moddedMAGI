# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Indicator(Component):
    """An Indicator component.
Display element at the corner of another element. For more information, see: https://mantine.dev/core/indicator/

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    Element that should have an indicator.

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- className (string; optional):
    Often used with CSS to style elements with common properties.

- classNames (dict; optional):
    add class names to Mantine components.

- color (boolean | number | string | dict | list; optional):
    Color from theme.colors or any other valid CSS color value.

- disabled (boolean; optional):
    When component is disabled it renders children without indicator.

- dot (boolean; optional):
    Whether to show the dot.

- inline (boolean; optional):
    Determines whether indicator container should be an inline
    element.

- label (a list of or a singular dash component, string or number; optional):
    Indicator label.

- offset (number; optional):
    Changes position offset, usually used when element has
    border-radius.

- overflowCount (number; optional):
    Indicator count overflowCount.

- position (a value equal to: 'top-center', 'top-end', 'top-start', 'bottom-center', 'bottom-end', 'bottom-start', 'middle-center', 'middle-end', 'middle-start'; optional):
    Indicator position relative to child element.

- processing (boolean; optional):
    Indicator processing animation.

- radius (number; optional):
    border-radius from theme.radius or number value to set radius in
    px.

- showZero (boolean; optional):
    When showZero is True and label is zero  renders children with
    indicator.

- size (number; optional):
    Size in px.

- style (boolean | number | string | dict | list; optional):
    Inline style.

- styles (boolean | number | string | dict | list; optional):
    Mantine styles API.

- sx (boolean | number | string | dict | list; optional):
    With sx you can add styles to component root element. If you need
    to customize styles of other elements within component use styles
    prop.

- withBorder (boolean; optional):
    Determines whether indicator should have border.

- zIndex (number; optional):
    Indicator z-index."""
    _children_props = ['label']
    _base_nodes = ['label', 'children']
    _namespace = 'dash_mantine_components'
    _type = 'Indicator'
    @_explicitize_args
    def __init__(self, children=None, position=Component.UNDEFINED, offset=Component.UNDEFINED, inline=Component.UNDEFINED, size=Component.UNDEFINED, label=Component.UNDEFINED, overflowCount=Component.UNDEFINED, dot=Component.UNDEFINED, radius=Component.UNDEFINED, color=Component.UNDEFINED, withBorder=Component.UNDEFINED, disabled=Component.UNDEFINED, showZero=Component.UNDEFINED, processing=Component.UNDEFINED, zIndex=Component.UNDEFINED, className=Component.UNDEFINED, classNames=Component.UNDEFINED, style=Component.UNDEFINED, styles=Component.UNDEFINED, id=Component.UNDEFINED, unstyled=Component.UNDEFINED, sx=Component.UNDEFINED, m=Component.UNDEFINED, my=Component.UNDEFINED, mx=Component.UNDEFINED, mt=Component.UNDEFINED, mb=Component.UNDEFINED, ml=Component.UNDEFINED, mr=Component.UNDEFINED, p=Component.UNDEFINED, py=Component.UNDEFINED, px=Component.UNDEFINED, pt=Component.UNDEFINED, pb=Component.UNDEFINED, pl=Component.UNDEFINED, pr=Component.UNDEFINED, bg=Component.UNDEFINED, c=Component.UNDEFINED, opacity=Component.UNDEFINED, ff=Component.UNDEFINED, fz=Component.UNDEFINED, fw=Component.UNDEFINED, lts=Component.UNDEFINED, ta=Component.UNDEFINED, lh=Component.UNDEFINED, fs=Component.UNDEFINED, tt=Component.UNDEFINED, td=Component.UNDEFINED, w=Component.UNDEFINED, miw=Component.UNDEFINED, maw=Component.UNDEFINED, h=Component.UNDEFINED, mih=Component.UNDEFINED, mah=Component.UNDEFINED, bgsz=Component.UNDEFINED, bgp=Component.UNDEFINED, bgr=Component.UNDEFINED, pos=Component.UNDEFINED, top=Component.UNDEFINED, left=Component.UNDEFINED, bottom=Component.UNDEFINED, right=Component.UNDEFINED, inset=Component.UNDEFINED, display=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'bg', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'color', 'disabled', 'display', 'dot', 'ff', 'fs', 'fw', 'fz', 'h', 'inline', 'inset', 'label', 'left', 'lh', 'lts', 'm', 'mah', 'maw', 'mb', 'mih', 'miw', 'ml', 'mr', 'mt', 'mx', 'my', 'offset', 'opacity', 'overflowCount', 'p', 'pb', 'pl', 'pos', 'position', 'pr', 'processing', 'pt', 'px', 'py', 'radius', 'right', 'showZero', 'size', 'style', 'styles', 'sx', 'ta', 'td', 'top', 'tt', 'unstyled', 'w', 'withBorder', 'zIndex']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'bg', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'color', 'disabled', 'display', 'dot', 'ff', 'fs', 'fw', 'fz', 'h', 'inline', 'inset', 'label', 'left', 'lh', 'lts', 'm', 'mah', 'maw', 'mb', 'mih', 'miw', 'ml', 'mr', 'mt', 'mx', 'my', 'offset', 'opacity', 'overflowCount', 'p', 'pb', 'pl', 'pos', 'position', 'pr', 'processing', 'pt', 'px', 'py', 'radius', 'right', 'showZero', 'size', 'style', 'styles', 'sx', 'ta', 'td', 'top', 'tt', 'unstyled', 'w', 'withBorder', 'zIndex']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Indicator, self).__init__(children=children, **args)
