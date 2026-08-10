# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class NotificationsProvider(Component):
    """A NotificationsProvider component.
Mantine notifications system. For more information, see: https://mantine.dev/others/notifications/

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    Your application.

- autoClose (number; optional):
    Auto close timeout for all notifications, False to disable auto
    close, can be overwritten for individual notifications by
    showNotification function.

- containerWidth (number; optional):
    Notification width in px, cannot exceed 100%.

- limit (number; optional):
    Maximum amount of notifications displayed at a time, other new
    notifications will be added to queue.

- notificationMaxHeight (number; optional):
    Notification max-height in px, used for transitions.

- position (a value equal to: 'top-left', 'top-right', 'top-center', 'bottom-left', 'bottom-right', 'bottom-center'; optional):
    Notifications position.

- transitionDuration (number; optional):
    Notification transitions duration, 0 to turn transitions off.

- zIndex (number; optional):
    Notifications container z-index."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_mantine_components'
    _type = 'NotificationsProvider'
    @_explicitize_args
    def __init__(self, children=None, position=Component.UNDEFINED, autoClose=Component.UNDEFINED, transitionDuration=Component.UNDEFINED, containerWidth=Component.UNDEFINED, notificationMaxHeight=Component.UNDEFINED, limit=Component.UNDEFINED, zIndex=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'autoClose', 'containerWidth', 'limit', 'notificationMaxHeight', 'position', 'transitionDuration', 'zIndex']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'autoClose', 'containerWidth', 'limit', 'notificationMaxHeight', 'position', 'transitionDuration', 'zIndex']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(NotificationsProvider, self).__init__(children=children, **args)
