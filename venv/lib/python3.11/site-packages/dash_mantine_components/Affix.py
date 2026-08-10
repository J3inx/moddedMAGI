# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Affix(Component):
    """An Affix component.
Render react node inside portal at fixed position. For more information, see: https://mantine.dev/core/affix/

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    Content.

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- className (string; optional):
    Often used with CSS to style elements with common properties.

- classNames (dict; optional):
    add class names to Mantine components.

- position (dict; optional):
    Fixed position in px, defaults to { bottom: 0, right: 0 }.

    `position` is a dict with keys:

    - bottom (string | number; optional)

    - left (string | number; optional)

    - right (string | number; optional)

    - top (string | number; optional)

- style (boolean | number | string | dict | list; optional):
    Inline style.

- styles (boolean | number | string | dict | list; optional):
    Mantine styles API.

- sx (boolean | number | string | dict | list; optional):
    With sx you can add styles to component root element. If you need
    to customize styles of other elements within component use styles
    prop.

- zIndex (number; optional):
    Root element z-index property."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_mantine_components'
    _type = 'Affix'
    @_explicitize_args
    def __init__(self, children=None, zIndex=Component.UNDEFINED, position=Component.UNDEFINED, className=Component.UNDEFINED, classNames=Component.UNDEFINED, style=Component.UNDEFINED, styles=Component.UNDEFINED, id=Component.UNDEFINED, unstyled=Component.UNDEFINED, sx=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'className', 'classNames', 'position', 'style', 'styles', 'sx', 'unstyled', 'zIndex']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'classNames', 'position', 'style', 'styles', 'sx', 'unstyled', 'zIndex']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Affix, self).__init__(children=children, **args)
