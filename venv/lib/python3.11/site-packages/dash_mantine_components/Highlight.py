# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Highlight(Component):
    """A Highlight component.
Highlight given part of a string with mark tag. For more information, see: https://mantine.dev/core/app-shell/

Keyword arguments:

- children (string; optional):
    Content.

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- align (a value equal to: 'initial', 'inherit', 'left', 'right', 'center', 'justify', 'end', 'start', '-moz-initial', 'revert', 'unset', 'match-parent'; optional):
    Sets text-align css property.

- className (string; optional):
    Often used with CSS to style elements with common properties.

- classNames (dict; optional):
    add class names to Mantine components.

- color (boolean | number | string | dict | list; optional):
    Key of theme.colors or any valid CSS color.

- gradient (dict; optional):
    Controls gradient settings in gradient variant only.

    `gradient` is a dict with keys:

    - deg (number; optional)

    - from (string; required)

    - to (string; required)

- highlight (string | list of strings; required):
    Substring or an array of substrings to highlight in children.

- highlightColor (boolean | number | string | dict | list; optional):
    Color from theme that is used for highlighting.

- inherit (boolean; optional):
    Inherit font properties from parent element.

- inline (boolean; optional):
    Sets line-height to 1 for centering.

- italic (boolean; optional):
    Adds font-style: italic style.

- lineClamp (number; optional):
    CSS -webkit-line-clamp property.

- size (number; optional):
    Key of theme.fontSizes or number to set font-size in px.

- span (boolean; optional):
    Shorthand for component=\"span\".

- strikethrough (boolean; optional):
    Add strikethrough styles.

- style (boolean | number | string | dict | list; optional):
    Inline style.

- styles (boolean | number | string | dict | list; optional):
    Mantine styles API.

- sx (boolean | number | string | dict | list; optional):
    With sx you can add styles to component root element. If you need
    to customize styles of other elements within component use styles
    prop.

- transform (a value equal to: 'initial', 'inherit', 'none', 'capitalize', 'uppercase', 'lowercase', '-moz-initial', 'revert', 'unset', 'full-size-kana', 'full-width'; optional):
    Sets text-transform css property.

- truncate (boolean | number | string | dict | list; optional):
    CSS truncate overflowing text with an ellipsis.

- underline (boolean; optional):
    Underline the text.

- variant (a value equal to: 'gradient', 'text', 'link'; optional):
    Link or text variant.

- weight (number; optional):
    Sets font-weight css property."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_mantine_components'
    _type = 'Highlight'
    @_explicitize_args
    def __init__(self, children=None, highlight=Component.REQUIRED, highlightColor=Component.UNDEFINED, size=Component.UNDEFINED, color=Component.UNDEFINED, weight=Component.UNDEFINED, truncate=Component.UNDEFINED, transform=Component.UNDEFINED, align=Component.UNDEFINED, variant=Component.UNDEFINED, lineClamp=Component.UNDEFINED, inline=Component.UNDEFINED, underline=Component.UNDEFINED, strikethrough=Component.UNDEFINED, italic=Component.UNDEFINED, inherit=Component.UNDEFINED, gradient=Component.UNDEFINED, span=Component.UNDEFINED, className=Component.UNDEFINED, classNames=Component.UNDEFINED, style=Component.UNDEFINED, styles=Component.UNDEFINED, id=Component.UNDEFINED, unstyled=Component.UNDEFINED, sx=Component.UNDEFINED, m=Component.UNDEFINED, my=Component.UNDEFINED, mx=Component.UNDEFINED, mt=Component.UNDEFINED, mb=Component.UNDEFINED, ml=Component.UNDEFINED, mr=Component.UNDEFINED, p=Component.UNDEFINED, py=Component.UNDEFINED, px=Component.UNDEFINED, pt=Component.UNDEFINED, pb=Component.UNDEFINED, pl=Component.UNDEFINED, pr=Component.UNDEFINED, bg=Component.UNDEFINED, c=Component.UNDEFINED, opacity=Component.UNDEFINED, ff=Component.UNDEFINED, fz=Component.UNDEFINED, fw=Component.UNDEFINED, lts=Component.UNDEFINED, ta=Component.UNDEFINED, lh=Component.UNDEFINED, fs=Component.UNDEFINED, tt=Component.UNDEFINED, td=Component.UNDEFINED, w=Component.UNDEFINED, miw=Component.UNDEFINED, maw=Component.UNDEFINED, h=Component.UNDEFINED, mih=Component.UNDEFINED, mah=Component.UNDEFINED, bgsz=Component.UNDEFINED, bgp=Component.UNDEFINED, bgr=Component.UNDEFINED, pos=Component.UNDEFINED, top=Component.UNDEFINED, left=Component.UNDEFINED, bottom=Component.UNDEFINED, right=Component.UNDEFINED, inset=Component.UNDEFINED, display=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'align', 'bg', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'color', 'display', 'ff', 'fs', 'fw', 'fz', 'gradient', 'h', 'highlight', 'highlightColor', 'inherit', 'inline', 'inset', 'italic', 'left', 'lh', 'lineClamp', 'lts', 'm', 'mah', 'maw', 'mb', 'mih', 'miw', 'ml', 'mr', 'mt', 'mx', 'my', 'opacity', 'p', 'pb', 'pl', 'pos', 'pr', 'pt', 'px', 'py', 'right', 'size', 'span', 'strikethrough', 'style', 'styles', 'sx', 'ta', 'td', 'top', 'transform', 'truncate', 'tt', 'underline', 'unstyled', 'variant', 'w', 'weight']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'align', 'bg', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'color', 'display', 'ff', 'fs', 'fw', 'fz', 'gradient', 'h', 'highlight', 'highlightColor', 'inherit', 'inline', 'inset', 'italic', 'left', 'lh', 'lineClamp', 'lts', 'm', 'mah', 'maw', 'mb', 'mih', 'miw', 'ml', 'mr', 'mt', 'mx', 'my', 'opacity', 'p', 'pb', 'pl', 'pos', 'pr', 'pt', 'px', 'py', 'right', 'size', 'span', 'strikethrough', 'style', 'styles', 'sx', 'ta', 'td', 'top', 'transform', 'truncate', 'tt', 'underline', 'unstyled', 'variant', 'w', 'weight']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['highlight']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(Highlight, self).__init__(children=children, **args)
