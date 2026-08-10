# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Prism(Component):
    """A Prism component.
Renders white or dark background depending on color scheme. For more information, see: https://mantine.dev/core/paper/

Keyword arguments:

- children (string; optional):
    Code which will be highlighted.

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- className (string; optional):
    Often used with CSS to style elements with common properties.

- classNames (dict; optional):
    add class names to Mantine components.

- colorScheme (a value equal to: 'light', 'dark'; optional):
    Force color scheme, defaults to theme.colorScheme.

- highlightLines (dict; optional):
    Highlight line at given line number with color from theme.colors.

    `highlightLines` is a dict with keys:


- language (a value equal to: 'c', 'markup', 'bash', 'clike', 'cpp', 'css', 'javascript', 'jsx', 'coffeescript', 'actionscript', 'css-extr', 'diff', 'git', 'go', 'graphql', 'handlebars', 'json', 'less', 'makefile', 'markdown', 'objectivec', 'ocaml', 'python', 'reason', 'sass', 'scss', 'sql', 'stylus', 'tsx', 'typescript', 'wasm', 'yaml'; required):
    Programming language that should be highlighted.

- noCopy (boolean; optional):
    True to remove copy to clipboard button.

- radius (number; optional):
    Key of theme.radius or number to set border-radius in px.

- style (boolean | number | string | dict | list; optional):
    Inline style.

- styles (boolean | number | string | dict | list; optional):
    Mantine styles API.

- sx (boolean | number | string | dict | list; optional):
    With sx you can add styles to component root element. If you need
    to customize styles of other elements within component use styles
    prop.

- trim (boolean; optional):
    Defines whether the code should be trimmed, defaults to True.

- withLineNumbers (boolean; optional):
    Display line numbers."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_mantine_components'
    _type = 'Prism'
    @_explicitize_args
    def __init__(self, children=None, language=Component.REQUIRED, noCopy=Component.UNDEFINED, withLineNumbers=Component.UNDEFINED, highlightLines=Component.UNDEFINED, colorScheme=Component.UNDEFINED, trim=Component.UNDEFINED, radius=Component.UNDEFINED, className=Component.UNDEFINED, classNames=Component.UNDEFINED, style=Component.UNDEFINED, styles=Component.UNDEFINED, id=Component.UNDEFINED, unstyled=Component.UNDEFINED, sx=Component.UNDEFINED, m=Component.UNDEFINED, my=Component.UNDEFINED, mx=Component.UNDEFINED, mt=Component.UNDEFINED, mb=Component.UNDEFINED, ml=Component.UNDEFINED, mr=Component.UNDEFINED, p=Component.UNDEFINED, py=Component.UNDEFINED, px=Component.UNDEFINED, pt=Component.UNDEFINED, pb=Component.UNDEFINED, pl=Component.UNDEFINED, pr=Component.UNDEFINED, bg=Component.UNDEFINED, c=Component.UNDEFINED, opacity=Component.UNDEFINED, ff=Component.UNDEFINED, fz=Component.UNDEFINED, fw=Component.UNDEFINED, lts=Component.UNDEFINED, ta=Component.UNDEFINED, lh=Component.UNDEFINED, fs=Component.UNDEFINED, tt=Component.UNDEFINED, td=Component.UNDEFINED, w=Component.UNDEFINED, miw=Component.UNDEFINED, maw=Component.UNDEFINED, h=Component.UNDEFINED, mih=Component.UNDEFINED, mah=Component.UNDEFINED, bgsz=Component.UNDEFINED, bgp=Component.UNDEFINED, bgr=Component.UNDEFINED, pos=Component.UNDEFINED, top=Component.UNDEFINED, left=Component.UNDEFINED, bottom=Component.UNDEFINED, right=Component.UNDEFINED, inset=Component.UNDEFINED, display=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'bg', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'colorScheme', 'display', 'ff', 'fs', 'fw', 'fz', 'h', 'highlightLines', 'inset', 'language', 'left', 'lh', 'lts', 'm', 'mah', 'maw', 'mb', 'mih', 'miw', 'ml', 'mr', 'mt', 'mx', 'my', 'noCopy', 'opacity', 'p', 'pb', 'pl', 'pos', 'pr', 'pt', 'px', 'py', 'radius', 'right', 'style', 'styles', 'sx', 'ta', 'td', 'top', 'trim', 'tt', 'unstyled', 'w', 'withLineNumbers']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'bg', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'colorScheme', 'display', 'ff', 'fs', 'fw', 'fz', 'h', 'highlightLines', 'inset', 'language', 'left', 'lh', 'lts', 'm', 'mah', 'maw', 'mb', 'mih', 'miw', 'ml', 'mr', 'mt', 'mx', 'my', 'noCopy', 'opacity', 'p', 'pb', 'pl', 'pos', 'pr', 'pt', 'px', 'py', 'radius', 'right', 'style', 'styles', 'sx', 'ta', 'td', 'top', 'trim', 'tt', 'unstyled', 'w', 'withLineNumbers']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['language']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(Prism, self).__init__(children=children, **args)
