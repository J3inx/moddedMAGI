# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class NavLink(Component):
    """A NavLink component.
Navigation link. For more information, see: https://mantine.dev/core/nav-link/

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    Child links.

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- active (boolean; optional):
    Determines whether link should have active styles.

- childrenOffset (number; optional):
    Key of theme.spacing or number to set collapsed links padding-left
    in px.

- className (string; optional):
    Often used with CSS to style elements with common properties.

- classNames (dict; optional):
    add class names to Mantine components.

- color (boolean | number | string | dict | list; optional):
    Key of theme.colors, active link color.

- description (a list of or a singular dash component, string or number; optional):
    Secondary link description.

- disableRightSectionRotation (boolean; optional):
    If set to True, right section will not rotate when collapse is
    opened.

- disabled (boolean; optional):
    Adds disabled styles to root element.

- href (string; optional):
    href.

- icon (a list of or a singular dash component, string or number; optional):
    Icon displayed on the left side of the label.

- label (a list of or a singular dash component, string or number; optional):
    Main link content.

- n_clicks (number; default 0):
    An integer that represents the number of times that this element
    has been clicked on.

- noWrap (boolean; optional):
    If prop is set then label and description will not wrap on the
    next line.

- opened (boolean; optional):
    Controlled nested items collapse state.

- refresh (boolean; optional):
    Whether to refresh the page.

- rightSection (a list of or a singular dash component, string or number; optional):
    Section displayed on the right side of the label.

- style (boolean | number | string | dict | list; optional):
    Inline style.

- styles (boolean | number | string | dict | list; optional):
    Mantine styles API.

- sx (boolean | number | string | dict | list; optional):
    With sx you can add styles to component root element. If you need
    to customize styles of other elements within component use styles
    prop.

- target (a value equal to: '_blank', '_self'; optional):
    Target.

- variant (a value equal to: 'subtle', 'filled', 'light'; optional):
    Active link variant."""
    _children_props = ['label', 'description', 'icon', 'rightSection']
    _base_nodes = ['label', 'description', 'icon', 'rightSection', 'children']
    _namespace = 'dash_mantine_components'
    _type = 'NavLink'
    @_explicitize_args
    def __init__(self, children=None, label=Component.UNDEFINED, description=Component.UNDEFINED, icon=Component.UNDEFINED, rightSection=Component.UNDEFINED, active=Component.UNDEFINED, color=Component.UNDEFINED, variant=Component.UNDEFINED, noWrap=Component.UNDEFINED, disableRightSectionRotation=Component.UNDEFINED, childrenOffset=Component.UNDEFINED, opened=Component.UNDEFINED, disabled=Component.UNDEFINED, n_clicks=Component.UNDEFINED, target=Component.UNDEFINED, href=Component.UNDEFINED, refresh=Component.UNDEFINED, className=Component.UNDEFINED, classNames=Component.UNDEFINED, style=Component.UNDEFINED, styles=Component.UNDEFINED, id=Component.UNDEFINED, unstyled=Component.UNDEFINED, sx=Component.UNDEFINED, m=Component.UNDEFINED, my=Component.UNDEFINED, mx=Component.UNDEFINED, mt=Component.UNDEFINED, mb=Component.UNDEFINED, ml=Component.UNDEFINED, mr=Component.UNDEFINED, p=Component.UNDEFINED, py=Component.UNDEFINED, px=Component.UNDEFINED, pt=Component.UNDEFINED, pb=Component.UNDEFINED, pl=Component.UNDEFINED, pr=Component.UNDEFINED, bg=Component.UNDEFINED, c=Component.UNDEFINED, opacity=Component.UNDEFINED, ff=Component.UNDEFINED, fz=Component.UNDEFINED, fw=Component.UNDEFINED, lts=Component.UNDEFINED, ta=Component.UNDEFINED, lh=Component.UNDEFINED, fs=Component.UNDEFINED, tt=Component.UNDEFINED, td=Component.UNDEFINED, w=Component.UNDEFINED, miw=Component.UNDEFINED, maw=Component.UNDEFINED, h=Component.UNDEFINED, mih=Component.UNDEFINED, mah=Component.UNDEFINED, bgsz=Component.UNDEFINED, bgp=Component.UNDEFINED, bgr=Component.UNDEFINED, pos=Component.UNDEFINED, top=Component.UNDEFINED, left=Component.UNDEFINED, bottom=Component.UNDEFINED, right=Component.UNDEFINED, inset=Component.UNDEFINED, display=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'active', 'bg', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'childrenOffset', 'className', 'classNames', 'color', 'description', 'disableRightSectionRotation', 'disabled', 'display', 'ff', 'fs', 'fw', 'fz', 'h', 'href', 'icon', 'inset', 'label', 'left', 'lh', 'lts', 'm', 'mah', 'maw', 'mb', 'mih', 'miw', 'ml', 'mr', 'mt', 'mx', 'my', 'n_clicks', 'noWrap', 'opacity', 'opened', 'p', 'pb', 'pl', 'pos', 'pr', 'pt', 'px', 'py', 'refresh', 'right', 'rightSection', 'style', 'styles', 'sx', 'ta', 'target', 'td', 'top', 'tt', 'unstyled', 'variant', 'w']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'active', 'bg', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'childrenOffset', 'className', 'classNames', 'color', 'description', 'disableRightSectionRotation', 'disabled', 'display', 'ff', 'fs', 'fw', 'fz', 'h', 'href', 'icon', 'inset', 'label', 'left', 'lh', 'lts', 'm', 'mah', 'maw', 'mb', 'mih', 'miw', 'ml', 'mr', 'mt', 'mx', 'my', 'n_clicks', 'noWrap', 'opacity', 'opened', 'p', 'pb', 'pl', 'pos', 'pr', 'pt', 'px', 'py', 'refresh', 'right', 'rightSection', 'style', 'styles', 'sx', 'ta', 'target', 'td', 'top', 'tt', 'unstyled', 'variant', 'w']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(NavLink, self).__init__(children=children, **args)
