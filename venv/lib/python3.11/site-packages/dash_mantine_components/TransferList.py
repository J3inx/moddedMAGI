# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class TransferList(Component):
    """A TransferList component.
Navigation link. For more information, see: https://mantine.dev/core/nav-link/

Keyword arguments:

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- breakpoint (number; optional):
    Breakpoint at which list will collapse to single column layout.

- className (string; optional):
    Often used with CSS to style elements with common properties.

- classNames (dict; optional):
    add class names to Mantine components.

- initialSelection (list of list of stringss; optional):
    Initial items selection.

- limit (number; optional):
    Limit amount of items showed at a time.

- listHeight (number; optional):
    List items height.

- nothingFound (boolean | number | string | dict | list; optional):
    Nothing found message.

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

- placeholder (boolean | number | string | dict | list; optional):
    Displayed when a list is empty and there is no search query.

- radius (number; optional):
    Predefined border-radius value from theme.radius or number for
    border-radius in px.

- searchPlaceholder (string | list of 2 elements: [string, string]; optional):
    Search fields placeholder.

- searchValues (list of 2 elements: [string, string]; optional):
    Controlled search queries.

- showTransferAll (boolean; optional):
    Whether to hide the transfer all button.

- style (boolean | number | string | dict | list; optional):
    Inline style.

- styles (boolean | number | string | dict | list; optional):
    Mantine styles API.

- sx (boolean | number | string | dict | list; optional):
    With sx you can add styles to component root element. If you need
    to customize styles of other elements within component use styles
    prop.

- titles (list of 2 elements: [string, string]; optional):
    Lists titles.

- transferAllMatchingFilter (boolean; optional):
    Whether to transfer only items matching the filter when clicking
    the transfer all control.

- value (boolean | number | string | dict | list; required):
    Current value."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_mantine_components'
    _type = 'TransferList'
    @_explicitize_args
    def __init__(self, value=Component.REQUIRED, initialSelection=Component.UNDEFINED, searchValues=Component.UNDEFINED, searchPlaceholder=Component.UNDEFINED, nothingFound=Component.UNDEFINED, placeholder=Component.UNDEFINED, titles=Component.UNDEFINED, listHeight=Component.UNDEFINED, breakpoint=Component.UNDEFINED, radius=Component.UNDEFINED, showTransferAll=Component.UNDEFINED, limit=Component.UNDEFINED, transferAllMatchingFilter=Component.UNDEFINED, persistence=Component.UNDEFINED, persisted_props=Component.UNDEFINED, persistence_type=Component.UNDEFINED, className=Component.UNDEFINED, classNames=Component.UNDEFINED, style=Component.UNDEFINED, styles=Component.UNDEFINED, id=Component.UNDEFINED, unstyled=Component.UNDEFINED, sx=Component.UNDEFINED, m=Component.UNDEFINED, my=Component.UNDEFINED, mx=Component.UNDEFINED, mt=Component.UNDEFINED, mb=Component.UNDEFINED, ml=Component.UNDEFINED, mr=Component.UNDEFINED, p=Component.UNDEFINED, py=Component.UNDEFINED, px=Component.UNDEFINED, pt=Component.UNDEFINED, pb=Component.UNDEFINED, pl=Component.UNDEFINED, pr=Component.UNDEFINED, bg=Component.UNDEFINED, c=Component.UNDEFINED, opacity=Component.UNDEFINED, ff=Component.UNDEFINED, fz=Component.UNDEFINED, fw=Component.UNDEFINED, lts=Component.UNDEFINED, ta=Component.UNDEFINED, lh=Component.UNDEFINED, fs=Component.UNDEFINED, tt=Component.UNDEFINED, td=Component.UNDEFINED, w=Component.UNDEFINED, miw=Component.UNDEFINED, maw=Component.UNDEFINED, h=Component.UNDEFINED, mih=Component.UNDEFINED, mah=Component.UNDEFINED, bgsz=Component.UNDEFINED, bgp=Component.UNDEFINED, bgr=Component.UNDEFINED, pos=Component.UNDEFINED, top=Component.UNDEFINED, left=Component.UNDEFINED, bottom=Component.UNDEFINED, right=Component.UNDEFINED, inset=Component.UNDEFINED, display=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'bg', 'bgp', 'bgr', 'bgsz', 'bottom', 'breakpoint', 'c', 'className', 'classNames', 'display', 'ff', 'fs', 'fw', 'fz', 'h', 'initialSelection', 'inset', 'left', 'lh', 'limit', 'listHeight', 'lts', 'm', 'mah', 'maw', 'mb', 'mih', 'miw', 'ml', 'mr', 'mt', 'mx', 'my', 'nothingFound', 'opacity', 'p', 'pb', 'persisted_props', 'persistence', 'persistence_type', 'pl', 'placeholder', 'pos', 'pr', 'pt', 'px', 'py', 'radius', 'right', 'searchPlaceholder', 'searchValues', 'showTransferAll', 'style', 'styles', 'sx', 'ta', 'td', 'titles', 'top', 'transferAllMatchingFilter', 'tt', 'unstyled', 'value', 'w']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'bg', 'bgp', 'bgr', 'bgsz', 'bottom', 'breakpoint', 'c', 'className', 'classNames', 'display', 'ff', 'fs', 'fw', 'fz', 'h', 'initialSelection', 'inset', 'left', 'lh', 'limit', 'listHeight', 'lts', 'm', 'mah', 'maw', 'mb', 'mih', 'miw', 'ml', 'mr', 'mt', 'mx', 'my', 'nothingFound', 'opacity', 'p', 'pb', 'persisted_props', 'persistence', 'persistence_type', 'pl', 'placeholder', 'pos', 'pr', 'pt', 'px', 'py', 'radius', 'right', 'searchPlaceholder', 'searchValues', 'showTransferAll', 'style', 'styles', 'sx', 'ta', 'td', 'titles', 'top', 'transferAllMatchingFilter', 'tt', 'unstyled', 'value', 'w']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['value']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(TransferList, self).__init__(**args)
