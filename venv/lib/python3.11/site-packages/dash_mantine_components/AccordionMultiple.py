# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AccordionMultiple(Component):
    """An AccordionMultiple component.
Divide content into collapsible sections. For more information, see: https://mantine.dev/core/accordion/

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    Accordion content.

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- chevron (a list of or a singular dash component, string or number; optional):
    Replaces chevron on all items.

- chevronPosition (a value equal to: 'left', 'right'; optional):
    Determines position of the chevron.

- chevronSize (number; optional):
    Chevron size in px.

- className (string; optional):
    Often used with CSS to style elements with common properties.

- classNames (dict; optional):
    add class names to Mantine components.

- disableChevronRotation (boolean; optional):
    Determines whether chevron rotation should be disabled.

- loop (boolean; optional):
    Determines whether arrow key presses should loop though items
    (first to last and last to first).

- order (a value equal to: 2, 3, 4, 5, 6; optional):
    Heading order, has no effect on visuals.

- radius (number; optional):
    border-radius from theme.radius or number to set value in px, will
    not be applied to default variant.

- style (boolean | number | string | dict | list; optional):
    Inline style.

- styles (boolean | number | string | dict | list; optional):
    Mantine styles API.

- sx (boolean | number | string | dict | list; optional):
    With sx you can add styles to component root element. If you need
    to customize styles of other elements within component use styles
    prop.

- transitionDuration (number; optional):
    Transition duration in ms, set 0 to disable transitions.

- value (list of strings; optional):
    Value that is used to manage accordion state.

- variant (a value equal to: 'default', 'contained', 'filled', 'separated'; optional):
    Controls visuals."""
    _children_props = ['chevron']
    _base_nodes = ['chevron', 'children']
    _namespace = 'dash_mantine_components'
    _type = 'AccordionMultiple'
    @_explicitize_args
    def __init__(self, children=None, value=Component.UNDEFINED, loop=Component.UNDEFINED, transitionDuration=Component.UNDEFINED, disableChevronRotation=Component.UNDEFINED, chevronPosition=Component.UNDEFINED, chevronSize=Component.UNDEFINED, order=Component.UNDEFINED, chevron=Component.UNDEFINED, variant=Component.UNDEFINED, radius=Component.UNDEFINED, className=Component.UNDEFINED, classNames=Component.UNDEFINED, style=Component.UNDEFINED, styles=Component.UNDEFINED, id=Component.UNDEFINED, unstyled=Component.UNDEFINED, sx=Component.UNDEFINED, m=Component.UNDEFINED, my=Component.UNDEFINED, mx=Component.UNDEFINED, mt=Component.UNDEFINED, mb=Component.UNDEFINED, ml=Component.UNDEFINED, mr=Component.UNDEFINED, p=Component.UNDEFINED, py=Component.UNDEFINED, px=Component.UNDEFINED, pt=Component.UNDEFINED, pb=Component.UNDEFINED, pl=Component.UNDEFINED, pr=Component.UNDEFINED, bg=Component.UNDEFINED, c=Component.UNDEFINED, opacity=Component.UNDEFINED, ff=Component.UNDEFINED, fz=Component.UNDEFINED, fw=Component.UNDEFINED, lts=Component.UNDEFINED, ta=Component.UNDEFINED, lh=Component.UNDEFINED, fs=Component.UNDEFINED, tt=Component.UNDEFINED, td=Component.UNDEFINED, w=Component.UNDEFINED, miw=Component.UNDEFINED, maw=Component.UNDEFINED, h=Component.UNDEFINED, mih=Component.UNDEFINED, mah=Component.UNDEFINED, bgsz=Component.UNDEFINED, bgp=Component.UNDEFINED, bgr=Component.UNDEFINED, pos=Component.UNDEFINED, top=Component.UNDEFINED, left=Component.UNDEFINED, bottom=Component.UNDEFINED, right=Component.UNDEFINED, inset=Component.UNDEFINED, display=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'bg', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'chevron', 'chevronPosition', 'chevronSize', 'className', 'classNames', 'disableChevronRotation', 'display', 'ff', 'fs', 'fw', 'fz', 'h', 'inset', 'left', 'lh', 'loop', 'lts', 'm', 'mah', 'maw', 'mb', 'mih', 'miw', 'ml', 'mr', 'mt', 'mx', 'my', 'opacity', 'order', 'p', 'pb', 'pl', 'pos', 'pr', 'pt', 'px', 'py', 'radius', 'right', 'style', 'styles', 'sx', 'ta', 'td', 'top', 'transitionDuration', 'tt', 'unstyled', 'value', 'variant', 'w']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'bg', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'chevron', 'chevronPosition', 'chevronSize', 'className', 'classNames', 'disableChevronRotation', 'display', 'ff', 'fs', 'fw', 'fz', 'h', 'inset', 'left', 'lh', 'loop', 'lts', 'm', 'mah', 'maw', 'mb', 'mih', 'miw', 'ml', 'mr', 'mt', 'mx', 'my', 'opacity', 'order', 'p', 'pb', 'pl', 'pos', 'pr', 'pt', 'px', 'py', 'radius', 'right', 'style', 'styles', 'sx', 'ta', 'td', 'top', 'transitionDuration', 'tt', 'unstyled', 'value', 'variant', 'w']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(AccordionMultiple, self).__init__(children=children, **args)
