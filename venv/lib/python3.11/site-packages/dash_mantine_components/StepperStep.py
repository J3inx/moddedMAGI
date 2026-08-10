# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class StepperStep(Component):
    """A StepperStep component.
Display content divided into a steps sequence. For more information, see: https://mantine.dev/core/stepper/

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    StepperStep content.

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- className (string; optional):
    Often used with CSS to style elements with common properties.

- classNames (dict; optional):
    add class names to Mantine components.

- color (boolean | number | string | dict | list; optional):
    Step color from theme.colors.

- completedIcon (a list of or a singular dash component, string or number; optional):
    Step icon displayed when step is completed.

- description (a list of or a singular dash component, string or number; optional):
    Step description.

- icon (a list of or a singular dash component, string or number; optional):
    Step icon, defaults to step index + 1 when rendered within
    Stepper.

- iconPosition (a value equal to: 'right', 'left'; optional):
    Icon position relative to step body.

- iconSize (number; optional):
    Icon wrapper size in px.

- label (a list of or a singular dash component, string or number; optional):
    Step label, render after icon.

- loading (boolean; optional):
    Indicates loading state on step.

- orientation (a value equal to: 'vertical', 'horizontal'; optional):
    Component orientation.

- progressIcon (a list of or a singular dash component, string or number; optional):
    Step icon displayed when step is in progress.

- radius (number; optional):
    Radius from theme.radius, or number to set border-radius in px.

- size (a value equal to: 'xs', 'sm', 'md', 'lg', 'xl'; optional):
    Component size.

- style (boolean | number | string | dict | list; optional):
    Inline style.

- styles (boolean | number | string | dict | list; optional):
    Mantine styles API.

- sx (boolean | number | string | dict | list; optional):
    With sx you can add styles to component root element. If you need
    to customize styles of other elements within component use styles
    prop.

- withIcon (boolean; optional):
    Should icon be displayed."""
    _children_props = ['icon', 'completedIcon', 'progressIcon', 'label', 'description']
    _base_nodes = ['icon', 'completedIcon', 'progressIcon', 'label', 'description', 'children']
    _namespace = 'dash_mantine_components'
    _type = 'StepperStep'
    @_explicitize_args
    def __init__(self, children=None, color=Component.UNDEFINED, withIcon=Component.UNDEFINED, icon=Component.UNDEFINED, completedIcon=Component.UNDEFINED, progressIcon=Component.UNDEFINED, label=Component.UNDEFINED, description=Component.UNDEFINED, iconSize=Component.UNDEFINED, iconPosition=Component.UNDEFINED, size=Component.UNDEFINED, radius=Component.UNDEFINED, loading=Component.UNDEFINED, orientation=Component.UNDEFINED, className=Component.UNDEFINED, classNames=Component.UNDEFINED, style=Component.UNDEFINED, styles=Component.UNDEFINED, id=Component.UNDEFINED, unstyled=Component.UNDEFINED, sx=Component.UNDEFINED, m=Component.UNDEFINED, my=Component.UNDEFINED, mx=Component.UNDEFINED, mt=Component.UNDEFINED, mb=Component.UNDEFINED, ml=Component.UNDEFINED, mr=Component.UNDEFINED, p=Component.UNDEFINED, py=Component.UNDEFINED, px=Component.UNDEFINED, pt=Component.UNDEFINED, pb=Component.UNDEFINED, pl=Component.UNDEFINED, pr=Component.UNDEFINED, bg=Component.UNDEFINED, c=Component.UNDEFINED, opacity=Component.UNDEFINED, ff=Component.UNDEFINED, fz=Component.UNDEFINED, fw=Component.UNDEFINED, lts=Component.UNDEFINED, ta=Component.UNDEFINED, lh=Component.UNDEFINED, fs=Component.UNDEFINED, tt=Component.UNDEFINED, td=Component.UNDEFINED, w=Component.UNDEFINED, miw=Component.UNDEFINED, maw=Component.UNDEFINED, h=Component.UNDEFINED, mih=Component.UNDEFINED, mah=Component.UNDEFINED, bgsz=Component.UNDEFINED, bgp=Component.UNDEFINED, bgr=Component.UNDEFINED, pos=Component.UNDEFINED, top=Component.UNDEFINED, left=Component.UNDEFINED, bottom=Component.UNDEFINED, right=Component.UNDEFINED, inset=Component.UNDEFINED, display=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'bg', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'color', 'completedIcon', 'description', 'display', 'ff', 'fs', 'fw', 'fz', 'h', 'icon', 'iconPosition', 'iconSize', 'inset', 'label', 'left', 'lh', 'loading', 'lts', 'm', 'mah', 'maw', 'mb', 'mih', 'miw', 'ml', 'mr', 'mt', 'mx', 'my', 'opacity', 'orientation', 'p', 'pb', 'pl', 'pos', 'pr', 'progressIcon', 'pt', 'px', 'py', 'radius', 'right', 'size', 'style', 'styles', 'sx', 'ta', 'td', 'top', 'tt', 'unstyled', 'w', 'withIcon']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'bg', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'color', 'completedIcon', 'description', 'display', 'ff', 'fs', 'fw', 'fz', 'h', 'icon', 'iconPosition', 'iconSize', 'inset', 'label', 'left', 'lh', 'loading', 'lts', 'm', 'mah', 'maw', 'mb', 'mih', 'miw', 'ml', 'mr', 'mt', 'mx', 'my', 'opacity', 'orientation', 'p', 'pb', 'pl', 'pos', 'pr', 'progressIcon', 'pt', 'px', 'py', 'radius', 'right', 'size', 'style', 'styles', 'sx', 'ta', 'td', 'top', 'tt', 'unstyled', 'w', 'withIcon']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(StepperStep, self).__init__(children=children, **args)
