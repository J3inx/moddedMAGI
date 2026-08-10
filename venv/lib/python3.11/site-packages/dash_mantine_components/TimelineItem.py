# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class TimelineItem(Component):
    """A TimelineItem component.
Display list of events in chronological order. For more information, see: https://mantine.dev/core/timeline/

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    React node that will be rendered after title.

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- active (boolean; optional):
    Should this item be highlighted, controlled by Timeline component.

- align (a value equal to: 'right', 'left'; optional):
    Line and bullet position relative to item content, controlled by
    Timeline component.

- bullet (a list of or a singular dash component, string or number; optional):
    React node that should be rendered inside bullet – icon, image,
    avatar, etc.

- bulletSize (number; optional):
    Bullet width, height and border-radius in px, controlled by
    Timeline component.

- className (string; optional):
    Often used with CSS to style elements with common properties.

- classNames (dict; optional):
    add class names to Mantine components.

- color (boolean | number | string | dict | list; optional):
    Highlight color for active item.

- lineActive (boolean; optional):
    Should line of this item be highlighted, controlled by Timeline
    component.

- lineVariant (a value equal to: 'solid', 'dashed', 'dotted'; optional):
    Line border style.

- lineWidth (number; optional):
    Line border width in px, controlled by Timeline component.

- radius (number; optional):
    Radius from theme.radius, or number to set border-radius in px.

- style (boolean | number | string | dict | list; optional):
    Inline style.

- styles (boolean | number | string | dict | list; optional):
    Mantine styles API.

- sx (boolean | number | string | dict | list; optional):
    With sx you can add styles to component root element. If you need
    to customize styles of other elements within component use styles
    prop.

- title (a list of or a singular dash component, string or number; optional):
    Item title, rendered next to bullet."""
    _children_props = ['title', 'bullet']
    _base_nodes = ['title', 'bullet', 'children']
    _namespace = 'dash_mantine_components'
    _type = 'TimelineItem'
    @_explicitize_args
    def __init__(self, children=None, title=Component.UNDEFINED, bullet=Component.UNDEFINED, bulletSize=Component.UNDEFINED, radius=Component.UNDEFINED, active=Component.UNDEFINED, lineActive=Component.UNDEFINED, color=Component.UNDEFINED, align=Component.UNDEFINED, lineVariant=Component.UNDEFINED, lineWidth=Component.UNDEFINED, className=Component.UNDEFINED, classNames=Component.UNDEFINED, style=Component.UNDEFINED, styles=Component.UNDEFINED, id=Component.UNDEFINED, unstyled=Component.UNDEFINED, sx=Component.UNDEFINED, m=Component.UNDEFINED, my=Component.UNDEFINED, mx=Component.UNDEFINED, mt=Component.UNDEFINED, mb=Component.UNDEFINED, ml=Component.UNDEFINED, mr=Component.UNDEFINED, p=Component.UNDEFINED, py=Component.UNDEFINED, px=Component.UNDEFINED, pt=Component.UNDEFINED, pb=Component.UNDEFINED, pl=Component.UNDEFINED, pr=Component.UNDEFINED, bg=Component.UNDEFINED, c=Component.UNDEFINED, opacity=Component.UNDEFINED, ff=Component.UNDEFINED, fz=Component.UNDEFINED, fw=Component.UNDEFINED, lts=Component.UNDEFINED, ta=Component.UNDEFINED, lh=Component.UNDEFINED, fs=Component.UNDEFINED, tt=Component.UNDEFINED, td=Component.UNDEFINED, w=Component.UNDEFINED, miw=Component.UNDEFINED, maw=Component.UNDEFINED, h=Component.UNDEFINED, mih=Component.UNDEFINED, mah=Component.UNDEFINED, bgsz=Component.UNDEFINED, bgp=Component.UNDEFINED, bgr=Component.UNDEFINED, pos=Component.UNDEFINED, top=Component.UNDEFINED, left=Component.UNDEFINED, bottom=Component.UNDEFINED, right=Component.UNDEFINED, inset=Component.UNDEFINED, display=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'active', 'align', 'bg', 'bgp', 'bgr', 'bgsz', 'bottom', 'bullet', 'bulletSize', 'c', 'className', 'classNames', 'color', 'display', 'ff', 'fs', 'fw', 'fz', 'h', 'inset', 'left', 'lh', 'lineActive', 'lineVariant', 'lineWidth', 'lts', 'm', 'mah', 'maw', 'mb', 'mih', 'miw', 'ml', 'mr', 'mt', 'mx', 'my', 'opacity', 'p', 'pb', 'pl', 'pos', 'pr', 'pt', 'px', 'py', 'radius', 'right', 'style', 'styles', 'sx', 'ta', 'td', 'title', 'top', 'tt', 'unstyled', 'w']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'active', 'align', 'bg', 'bgp', 'bgr', 'bgsz', 'bottom', 'bullet', 'bulletSize', 'c', 'className', 'classNames', 'color', 'display', 'ff', 'fs', 'fw', 'fz', 'h', 'inset', 'left', 'lh', 'lineActive', 'lineVariant', 'lineWidth', 'lts', 'm', 'mah', 'maw', 'mb', 'mih', 'miw', 'ml', 'mr', 'mt', 'mx', 'my', 'opacity', 'p', 'pb', 'pl', 'pos', 'pr', 'pt', 'px', 'py', 'radius', 'right', 'style', 'styles', 'sx', 'ta', 'td', 'title', 'top', 'tt', 'unstyled', 'w']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(TimelineItem, self).__init__(children=children, **args)
