# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class LoadingOverlay(Component):
    """A LoadingOverlay component.
Similar to dcc.Loading, overlay over given container with centered Loader from Mantine Theme. For more information, see: https://mantine.dev/core/loading-overlay/

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    Content.

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- className (string; optional):
    Often used with CSS to style elements with common properties.

- classNames (dict; optional):
    add class names to Mantine components.

- exitTransitionDuration (number; optional):
    Exit transition duration in ms.

- loader (a list of or a singular dash component, string or number; optional):
    Provide custom loader.

- loaderProps (dict; optional):
    Loader component props.

    `loaderProps` is a dict with keys:

    - color (boolean | number | string | dict | list; optional):
        Loader color from theme.

    - size (number; optional):
        Defines width of loader.

    - variant (a value equal to: 'bars', 'oval', 'dots'; optional):
        Loader appearance.

- loading_state (dict; optional):
    Object that holds the loading state object coming from
    dash-renderer.

    `loading_state` is a dict with keys:

    - component_name (string; required):
        Holds the name of the component that is loading.

    - is_loading (boolean; required):
        Determines if the component is loading or not.

    - prop_name (string; required):
        Holds which property is loading.

- overlayBlur (number; optional):
    Sets overlay blur in px.

- overlayColor (string; optional):
    Sets overlay color, defaults to theme.white in light theme and to
    theme.colors.dark[5] in dark theme.

- overlayOpacity (number; optional):
    Sets overlay opacity.

- radius (number; optional):
    Value from theme.radius or number to set border-radius in px.

- style (boolean | number | string | dict | list; optional):
    Inline style.

- styles (boolean | number | string | dict | list; optional):
    Mantine styles API.

- sx (boolean | number | string | dict | list; optional):
    With sx you can add styles to component root element. If you need
    to customize styles of other elements within component use styles
    prop.

- transitionDuration (number; optional):
    Animation duration in ms.

- zIndex (number; optional):
    Loading overlay z-index."""
    _children_props = ['loader']
    _base_nodes = ['loader', 'children']
    _namespace = 'dash_mantine_components'
    _type = 'LoadingOverlay'
    @_explicitize_args
    def __init__(self, children=None, loader=Component.UNDEFINED, loaderProps=Component.UNDEFINED, overlayOpacity=Component.UNDEFINED, overlayColor=Component.UNDEFINED, overlayBlur=Component.UNDEFINED, zIndex=Component.UNDEFINED, transitionDuration=Component.UNDEFINED, exitTransitionDuration=Component.UNDEFINED, radius=Component.UNDEFINED, loading_state=Component.UNDEFINED, className=Component.UNDEFINED, classNames=Component.UNDEFINED, style=Component.UNDEFINED, styles=Component.UNDEFINED, id=Component.UNDEFINED, unstyled=Component.UNDEFINED, sx=Component.UNDEFINED, m=Component.UNDEFINED, my=Component.UNDEFINED, mx=Component.UNDEFINED, mt=Component.UNDEFINED, mb=Component.UNDEFINED, ml=Component.UNDEFINED, mr=Component.UNDEFINED, p=Component.UNDEFINED, py=Component.UNDEFINED, px=Component.UNDEFINED, pt=Component.UNDEFINED, pb=Component.UNDEFINED, pl=Component.UNDEFINED, pr=Component.UNDEFINED, bg=Component.UNDEFINED, c=Component.UNDEFINED, opacity=Component.UNDEFINED, ff=Component.UNDEFINED, fz=Component.UNDEFINED, fw=Component.UNDEFINED, lts=Component.UNDEFINED, ta=Component.UNDEFINED, lh=Component.UNDEFINED, fs=Component.UNDEFINED, tt=Component.UNDEFINED, td=Component.UNDEFINED, w=Component.UNDEFINED, miw=Component.UNDEFINED, maw=Component.UNDEFINED, h=Component.UNDEFINED, mih=Component.UNDEFINED, mah=Component.UNDEFINED, bgsz=Component.UNDEFINED, bgp=Component.UNDEFINED, bgr=Component.UNDEFINED, pos=Component.UNDEFINED, top=Component.UNDEFINED, left=Component.UNDEFINED, bottom=Component.UNDEFINED, right=Component.UNDEFINED, inset=Component.UNDEFINED, display=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'bg', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'display', 'exitTransitionDuration', 'ff', 'fs', 'fw', 'fz', 'h', 'inset', 'left', 'lh', 'loader', 'loaderProps', 'loading_state', 'lts', 'm', 'mah', 'maw', 'mb', 'mih', 'miw', 'ml', 'mr', 'mt', 'mx', 'my', 'opacity', 'overlayBlur', 'overlayColor', 'overlayOpacity', 'p', 'pb', 'pl', 'pos', 'pr', 'pt', 'px', 'py', 'radius', 'right', 'style', 'styles', 'sx', 'ta', 'td', 'top', 'transitionDuration', 'tt', 'unstyled', 'w', 'zIndex']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'bg', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'display', 'exitTransitionDuration', 'ff', 'fs', 'fw', 'fz', 'h', 'inset', 'left', 'lh', 'loader', 'loaderProps', 'loading_state', 'lts', 'm', 'mah', 'maw', 'mb', 'mih', 'miw', 'ml', 'mr', 'mt', 'mx', 'my', 'opacity', 'overlayBlur', 'overlayColor', 'overlayOpacity', 'p', 'pb', 'pl', 'pos', 'pr', 'pt', 'px', 'py', 'radius', 'right', 'style', 'styles', 'sx', 'ta', 'td', 'top', 'transitionDuration', 'tt', 'unstyled', 'w', 'zIndex']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(LoadingOverlay, self).__init__(children=children, **args)
