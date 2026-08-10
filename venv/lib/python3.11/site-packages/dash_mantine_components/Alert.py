# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Alert(Component):
    """An Alert component.
Attract user attention with important static message. For more information, see: https://mantine.dev/core/alert/

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    Alert message.

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- className (string; optional):
    Often used with CSS to style elements with common properties.

- classNames (dict; optional):
    add class names to Mantine components.

- closeButtonLabel (string; optional):
    Close button aria-label.

- color (boolean | number | string | dict | list; optional):
    Color from theme.colors.

- duration (number; optional):
    Duration in milliseconds after which the Alert dismisses itself.

- hide (boolean; default False):
    Whether to hide the alert.

- icon (a list of or a singular dash component, string or number; optional):
    Icon displayed next to title.

- radius (number; optional):
    Radius from theme.radius, or number to set border-radius in px,
    defaults to theme.defaultRadius.

- style (boolean | number | string | dict | list; optional):
    Inline style.

- styles (boolean | number | string | dict | list; optional):
    Mantine styles API.

- sx (boolean | number | string | dict | list; optional):
    With sx you can add styles to component root element. If you need
    to customize styles of other elements within component use styles
    prop.

- title (a list of or a singular dash component, string or number; optional):
    Alert title.

- variant (a value equal to: 'filled', 'outline', 'light'; optional):
    Controls Alert background, color and border styles, defaults to
    light.

- withCloseButton (boolean; optional):
    True to display close button."""
    _children_props = ['title', 'icon']
    _base_nodes = ['title', 'icon', 'children']
    _namespace = 'dash_mantine_components'
    _type = 'Alert'
    @_explicitize_args
    def __init__(self, children=None, title=Component.UNDEFINED, variant=Component.UNDEFINED, color=Component.UNDEFINED, icon=Component.UNDEFINED, withCloseButton=Component.UNDEFINED, radius=Component.UNDEFINED, duration=Component.UNDEFINED, hide=Component.UNDEFINED, closeButtonLabel=Component.UNDEFINED, className=Component.UNDEFINED, classNames=Component.UNDEFINED, style=Component.UNDEFINED, styles=Component.UNDEFINED, id=Component.UNDEFINED, unstyled=Component.UNDEFINED, sx=Component.UNDEFINED, m=Component.UNDEFINED, my=Component.UNDEFINED, mx=Component.UNDEFINED, mt=Component.UNDEFINED, mb=Component.UNDEFINED, ml=Component.UNDEFINED, mr=Component.UNDEFINED, p=Component.UNDEFINED, py=Component.UNDEFINED, px=Component.UNDEFINED, pt=Component.UNDEFINED, pb=Component.UNDEFINED, pl=Component.UNDEFINED, pr=Component.UNDEFINED, bg=Component.UNDEFINED, c=Component.UNDEFINED, opacity=Component.UNDEFINED, ff=Component.UNDEFINED, fz=Component.UNDEFINED, fw=Component.UNDEFINED, lts=Component.UNDEFINED, ta=Component.UNDEFINED, lh=Component.UNDEFINED, fs=Component.UNDEFINED, tt=Component.UNDEFINED, td=Component.UNDEFINED, w=Component.UNDEFINED, miw=Component.UNDEFINED, maw=Component.UNDEFINED, h=Component.UNDEFINED, mih=Component.UNDEFINED, mah=Component.UNDEFINED, bgsz=Component.UNDEFINED, bgp=Component.UNDEFINED, bgr=Component.UNDEFINED, pos=Component.UNDEFINED, top=Component.UNDEFINED, left=Component.UNDEFINED, bottom=Component.UNDEFINED, right=Component.UNDEFINED, inset=Component.UNDEFINED, display=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'bg', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'closeButtonLabel', 'color', 'display', 'duration', 'ff', 'fs', 'fw', 'fz', 'h', 'hide', 'icon', 'inset', 'left', 'lh', 'lts', 'm', 'mah', 'maw', 'mb', 'mih', 'miw', 'ml', 'mr', 'mt', 'mx', 'my', 'opacity', 'p', 'pb', 'pl', 'pos', 'pr', 'pt', 'px', 'py', 'radius', 'right', 'style', 'styles', 'sx', 'ta', 'td', 'title', 'top', 'tt', 'unstyled', 'variant', 'w', 'withCloseButton']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'bg', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'closeButtonLabel', 'color', 'display', 'duration', 'ff', 'fs', 'fw', 'fz', 'h', 'hide', 'icon', 'inset', 'left', 'lh', 'lts', 'm', 'mah', 'maw', 'mb', 'mih', 'miw', 'ml', 'mr', 'mt', 'mx', 'my', 'opacity', 'p', 'pb', 'pl', 'pos', 'pr', 'pt', 'px', 'py', 'radius', 'right', 'style', 'styles', 'sx', 'ta', 'td', 'title', 'top', 'tt', 'unstyled', 'variant', 'w', 'withCloseButton']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Alert, self).__init__(children=children, **args)
