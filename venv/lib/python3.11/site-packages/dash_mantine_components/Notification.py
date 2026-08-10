# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Notification(Component):
    """A Notification component.
Show dynamic notifications and alerts to user, part of notifications system. For more information, see: https://mantine.dev/others/notifications/

Keyword arguments:

- id (string; required):
    The ID of this component, used to identify dash components in
    callbacks.

- action (a value equal to: 'show', 'update', 'hide'; required):
    Action.

- autoClose (number; optional):
    Auto close timeout in milliseconds, False to disable auto close.

- className (string; optional):
    Often used with CSS to style elements with common properties.

- classNames (dict; optional):
    add class names to Mantine components.

- color (boolean | number | string | dict | list; optional):
    Notification line or icon color.

- disallowClose (boolean; optional):
    Removes close button.

- icon (a list of or a singular dash component, string or number; optional):
    Notification icon, replaces color line.

- loading (boolean; optional):
    Replaces colored line or icon with Loader component.

- message (a list of or a singular dash component, string or number; required):
    Notification body, place main text here.

- radius (a value equal to: 'xs', 'sm', 'md', 'lg', 'xl'; optional):
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
    Notification title, displayed before body."""
    _children_props = ['icon', 'title', 'message']
    _base_nodes = ['icon', 'title', 'message', 'children']
    _namespace = 'dash_mantine_components'
    _type = 'Notification'
    @_explicitize_args
    def __init__(self, color=Component.UNDEFINED, radius=Component.UNDEFINED, icon=Component.UNDEFINED, title=Component.UNDEFINED, message=Component.REQUIRED, loading=Component.UNDEFINED, disallowClose=Component.UNDEFINED, id=Component.REQUIRED, autoClose=Component.UNDEFINED, action=Component.REQUIRED, className=Component.UNDEFINED, classNames=Component.UNDEFINED, style=Component.UNDEFINED, styles=Component.UNDEFINED, unstyled=Component.UNDEFINED, sx=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'action', 'autoClose', 'className', 'classNames', 'color', 'disallowClose', 'icon', 'loading', 'message', 'radius', 'style', 'styles', 'sx', 'title', 'unstyled']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'action', 'autoClose', 'className', 'classNames', 'color', 'disallowClose', 'icon', 'loading', 'message', 'radius', 'style', 'styles', 'sx', 'title', 'unstyled']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['id', 'action', 'message']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(Notification, self).__init__(**args)
