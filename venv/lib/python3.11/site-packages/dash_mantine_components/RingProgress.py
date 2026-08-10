# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class RingProgress(Component):
    """A RingProgress component.
Give user feedback for status of the task with circle diagram. For more information, see: https://mantine.dev/core/ring-progress/

Keyword arguments:

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- className (string; optional):
    Often used with CSS to style elements with common properties.

- classNames (dict; optional):
    add class names to Mantine components.

- label (a list of or a singular dash component, string or number; optional):
    Label displayed in the center of the ring.

- rootColor (boolean | number | string | dict | list; optional):
    Color of the root section, key of theme.colors or CSS color value.

- roundCaps (boolean; optional):
    Sets whether the edges of the progress circle are rounded.

- sections (list of dicts; required):
    Ring sections.

    `sections` is a list of dicts with keys:

    - color (boolean | number | string | dict | list; required)

    - tooltip (a list of or a singular dash component, string or number; optional)

    - value (number; required)

- size (number; optional):
    Width and height of the progress ring in px.

- style (boolean | number | string | dict | list; optional):
    Inline style.

- styles (boolean | number | string | dict | list; optional):
    Mantine styles API.

- sx (boolean | number | string | dict | list; optional):
    With sx you can add styles to component root element. If you need
    to customize styles of other elements within component use styles
    prop.

- thickness (number; optional):
    Ring thickness."""
    _children_props = ['label', 'sections[].tooltip']
    _base_nodes = ['label', 'children']
    _namespace = 'dash_mantine_components'
    _type = 'RingProgress'
    @_explicitize_args
    def __init__(self, label=Component.UNDEFINED, thickness=Component.UNDEFINED, size=Component.UNDEFINED, roundCaps=Component.UNDEFINED, sections=Component.REQUIRED, rootColor=Component.UNDEFINED, className=Component.UNDEFINED, classNames=Component.UNDEFINED, style=Component.UNDEFINED, styles=Component.UNDEFINED, id=Component.UNDEFINED, unstyled=Component.UNDEFINED, sx=Component.UNDEFINED, m=Component.UNDEFINED, my=Component.UNDEFINED, mx=Component.UNDEFINED, mt=Component.UNDEFINED, mb=Component.UNDEFINED, ml=Component.UNDEFINED, mr=Component.UNDEFINED, p=Component.UNDEFINED, py=Component.UNDEFINED, px=Component.UNDEFINED, pt=Component.UNDEFINED, pb=Component.UNDEFINED, pl=Component.UNDEFINED, pr=Component.UNDEFINED, bg=Component.UNDEFINED, c=Component.UNDEFINED, opacity=Component.UNDEFINED, ff=Component.UNDEFINED, fz=Component.UNDEFINED, fw=Component.UNDEFINED, lts=Component.UNDEFINED, ta=Component.UNDEFINED, lh=Component.UNDEFINED, fs=Component.UNDEFINED, tt=Component.UNDEFINED, td=Component.UNDEFINED, w=Component.UNDEFINED, miw=Component.UNDEFINED, maw=Component.UNDEFINED, h=Component.UNDEFINED, mih=Component.UNDEFINED, mah=Component.UNDEFINED, bgsz=Component.UNDEFINED, bgp=Component.UNDEFINED, bgr=Component.UNDEFINED, pos=Component.UNDEFINED, top=Component.UNDEFINED, left=Component.UNDEFINED, bottom=Component.UNDEFINED, right=Component.UNDEFINED, inset=Component.UNDEFINED, display=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'bg', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'display', 'ff', 'fs', 'fw', 'fz', 'h', 'inset', 'label', 'left', 'lh', 'lts', 'm', 'mah', 'maw', 'mb', 'mih', 'miw', 'ml', 'mr', 'mt', 'mx', 'my', 'opacity', 'p', 'pb', 'pl', 'pos', 'pr', 'pt', 'px', 'py', 'right', 'rootColor', 'roundCaps', 'sections', 'size', 'style', 'styles', 'sx', 'ta', 'td', 'thickness', 'top', 'tt', 'unstyled', 'w']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'bg', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'display', 'ff', 'fs', 'fw', 'fz', 'h', 'inset', 'label', 'left', 'lh', 'lts', 'm', 'mah', 'maw', 'mb', 'mih', 'miw', 'ml', 'mr', 'mt', 'mx', 'my', 'opacity', 'p', 'pb', 'pl', 'pos', 'pr', 'pt', 'px', 'py', 'right', 'rootColor', 'roundCaps', 'sections', 'size', 'style', 'styles', 'sx', 'ta', 'td', 'thickness', 'top', 'tt', 'unstyled', 'w']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['sections']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(RingProgress, self).__init__(**args)
