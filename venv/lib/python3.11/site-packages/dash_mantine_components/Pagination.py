# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Pagination(Component):
    """A Pagination component.
Display active page and navigate between multiple pages. For more information, see: https://mantine.dev/core/pagination/

Keyword arguments:

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- align (a value equal to: 'initial', 'inherit', 'left', 'right', 'center', 'justify', 'end', 'start', '-moz-initial', 'revert', 'unset', 'match-parent'; optional):
    Defines align-items css property.

- boundaries (number; optional):
    Amount of elements visible on left/right edges.

- className (string; optional):
    Often used with CSS to style elements with common properties.

- classNames (dict; optional):
    add class names to Mantine components.

- color (boolean | number | string | dict | list; optional):
    Active item color from theme, defaults to theme.primaryColor.

- disabled (boolean; optional):
    Determines whether all controls should be disabled.

- grow (boolean; optional):
    Defines flex-grow property for each element, True -> 1, False ->
    0.

- noWrap (boolean; optional):
    Defined flex-wrap property.

- page (number; optional):
    Controlled active page number.

- persisted_props (list of strings; default ["page"]):
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

- position (a value equal to: 'left', 'right', 'center', 'apart'; optional):
    Defines justify-content property.

- radius (number; optional):
    Predefined item radius or number to set border-radius in px.

- siblings (number; optional):
    Siblings amount on left/right side of selected page.

- size (number; optional):
    Predefined item size or number to set width and height in px.

- spacing (number; optional):
    Spacing between items from theme or number to set value in px,
    defaults to theme.spacing.xs / 2.

- style (boolean | number | string | dict | list; optional):
    Inline style.

- styles (boolean | number | string | dict | list; optional):
    Mantine styles API.

- sx (boolean | number | string | dict | list; optional):
    With sx you can add styles to component root element. If you need
    to customize styles of other elements within component use styles
    prop.

- total (number; required):
    Total amount of pages.

- withControls (boolean; optional):
    Show/hide prev/next controls.

- withEdges (boolean; optional):
    Show/hide jump to start/end controls."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_mantine_components'
    _type = 'Pagination'
    @_explicitize_args
    def __init__(self, color=Component.UNDEFINED, page=Component.UNDEFINED, total=Component.REQUIRED, siblings=Component.UNDEFINED, boundaries=Component.UNDEFINED, spacing=Component.UNDEFINED, size=Component.UNDEFINED, radius=Component.UNDEFINED, withEdges=Component.UNDEFINED, withControls=Component.UNDEFINED, disabled=Component.UNDEFINED, position=Component.UNDEFINED, noWrap=Component.UNDEFINED, grow=Component.UNDEFINED, align=Component.UNDEFINED, className=Component.UNDEFINED, classNames=Component.UNDEFINED, style=Component.UNDEFINED, styles=Component.UNDEFINED, id=Component.UNDEFINED, unstyled=Component.UNDEFINED, sx=Component.UNDEFINED, m=Component.UNDEFINED, my=Component.UNDEFINED, mx=Component.UNDEFINED, mt=Component.UNDEFINED, mb=Component.UNDEFINED, ml=Component.UNDEFINED, mr=Component.UNDEFINED, p=Component.UNDEFINED, py=Component.UNDEFINED, px=Component.UNDEFINED, pt=Component.UNDEFINED, pb=Component.UNDEFINED, pl=Component.UNDEFINED, pr=Component.UNDEFINED, bg=Component.UNDEFINED, c=Component.UNDEFINED, opacity=Component.UNDEFINED, ff=Component.UNDEFINED, fz=Component.UNDEFINED, fw=Component.UNDEFINED, lts=Component.UNDEFINED, ta=Component.UNDEFINED, lh=Component.UNDEFINED, fs=Component.UNDEFINED, tt=Component.UNDEFINED, td=Component.UNDEFINED, w=Component.UNDEFINED, miw=Component.UNDEFINED, maw=Component.UNDEFINED, h=Component.UNDEFINED, mih=Component.UNDEFINED, mah=Component.UNDEFINED, bgsz=Component.UNDEFINED, bgp=Component.UNDEFINED, bgr=Component.UNDEFINED, pos=Component.UNDEFINED, top=Component.UNDEFINED, left=Component.UNDEFINED, bottom=Component.UNDEFINED, right=Component.UNDEFINED, inset=Component.UNDEFINED, display=Component.UNDEFINED, persistence=Component.UNDEFINED, persisted_props=Component.UNDEFINED, persistence_type=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'align', 'bg', 'bgp', 'bgr', 'bgsz', 'bottom', 'boundaries', 'c', 'className', 'classNames', 'color', 'disabled', 'display', 'ff', 'fs', 'fw', 'fz', 'grow', 'h', 'inset', 'left', 'lh', 'lts', 'm', 'mah', 'maw', 'mb', 'mih', 'miw', 'ml', 'mr', 'mt', 'mx', 'my', 'noWrap', 'opacity', 'p', 'page', 'pb', 'persisted_props', 'persistence', 'persistence_type', 'pl', 'pos', 'position', 'pr', 'pt', 'px', 'py', 'radius', 'right', 'siblings', 'size', 'spacing', 'style', 'styles', 'sx', 'ta', 'td', 'top', 'total', 'tt', 'unstyled', 'w', 'withControls', 'withEdges']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'align', 'bg', 'bgp', 'bgr', 'bgsz', 'bottom', 'boundaries', 'c', 'className', 'classNames', 'color', 'disabled', 'display', 'ff', 'fs', 'fw', 'fz', 'grow', 'h', 'inset', 'left', 'lh', 'lts', 'm', 'mah', 'maw', 'mb', 'mih', 'miw', 'ml', 'mr', 'mt', 'mx', 'my', 'noWrap', 'opacity', 'p', 'page', 'pb', 'persisted_props', 'persistence', 'persistence_type', 'pl', 'pos', 'position', 'pr', 'pt', 'px', 'py', 'radius', 'right', 'siblings', 'size', 'spacing', 'style', 'styles', 'sx', 'ta', 'td', 'top', 'total', 'tt', 'unstyled', 'w', 'withControls', 'withEdges']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['total']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(Pagination, self).__init__(**args)
