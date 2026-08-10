# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class TooltipFloating(Component):
    """A TooltipFloating component.
Renders tooltip at given element on mouse over or any other event. For more information, see: https://mantine.dev/core/tooltip/

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    Target element.

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- className (string; optional):
    Often used with CSS to style elements with common properties.

- color (boolean | number | string | dict | list; optional):
    Key of theme.colors.

- disabled (boolean; optional):
    Disables tooltip.

- label (a list of or a singular dash component, string or number; required):
    Tooltip label.

- m (number; optional):
    margin props.

- mb (number; optional):
    margin props.

- ml (number; optional):
    margin props.

- mr (number; optional):
    margin props.

- mt (number; optional):
    margin props.

- multiline (boolean; optional):
    Defines whether content should be wrapped on to the next line.

- mx (number; optional):
    margin props.

- my (number; optional):
    margin props.

- offset (number; optional):
    Offset from mouse in px.

- p (number; optional):
    padding props.

- pb (number; optional):
    padding props.

- pl (number; optional):
    padding props.

- position (a value equal to: 'top', 'right', 'bottom', 'left', 'top-end', 'top-start', 'right-end', 'right-start', 'bottom-end', 'bottom-start', 'left-end', 'left-start'; optional):
    Tooltip position relative to target element (default) or mouse
    (floating).

- pr (number; optional):
    padding props.

- pt (number; optional):
    padding props.

- px (number; optional):
    padding props.

- py (number; optional):
    padding props.

- radius (number; optional):
    Radius from theme.radius or number to set border-radius in px.

- style (boolean | number | string | dict | list; optional):
    Inline style.

- styles (dict; optional):
    Mantine styles API.

- unstyled (boolean; optional):
    Remove all Mantine styling from the component.

- width (number; optional):
    Tooltip width in px.

- zIndex (number; optional):
    Tooltip z-index."""
    _children_props = ['label']
    _base_nodes = ['label', 'children']
    _namespace = 'dash_mantine_components'
    _type = 'TooltipFloating'
    @_explicitize_args
    def __init__(self, children=None, offset=Component.UNDEFINED, position=Component.UNDEFINED, label=Component.REQUIRED, radius=Component.UNDEFINED, color=Component.UNDEFINED, multiline=Component.UNDEFINED, width=Component.UNDEFINED, zIndex=Component.UNDEFINED, disabled=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, styles=Component.UNDEFINED, id=Component.UNDEFINED, unstyled=Component.UNDEFINED, m=Component.UNDEFINED, my=Component.UNDEFINED, mx=Component.UNDEFINED, mt=Component.UNDEFINED, mb=Component.UNDEFINED, ml=Component.UNDEFINED, mr=Component.UNDEFINED, p=Component.UNDEFINED, py=Component.UNDEFINED, px=Component.UNDEFINED, pt=Component.UNDEFINED, pb=Component.UNDEFINED, pl=Component.UNDEFINED, pr=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'className', 'color', 'disabled', 'label', 'm', 'mb', 'ml', 'mr', 'mt', 'multiline', 'mx', 'my', 'offset', 'p', 'pb', 'pl', 'position', 'pr', 'pt', 'px', 'py', 'radius', 'style', 'styles', 'unstyled', 'width', 'zIndex']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'color', 'disabled', 'label', 'm', 'mb', 'ml', 'mr', 'mt', 'multiline', 'mx', 'my', 'offset', 'p', 'pb', 'pl', 'position', 'pr', 'pt', 'px', 'py', 'radius', 'style', 'styles', 'unstyled', 'width', 'zIndex']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in ['label']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(TooltipFloating, self).__init__(children=children, **args)
