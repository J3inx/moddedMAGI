# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Image(Component):
    """An Image component.
Image with optional placeholder for loading and error state. For more information, see: https://mantine.dev/core/image/

Keyword arguments:

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- alt (string; optional):
    Image alt text, used as title for placeholder if image was not
    loaded.

- caption (a list of or a singular dash component, string or number; optional):
    Image figcaption, displayed bellow image.

- className (string; optional):
    Often used with CSS to style elements with common properties.

- classNames (dict; optional):
    add class names to Mantine components.

- fit (a value equal to: 'cover', 'contain'; optional):
    Image object-fit property.

- height (string | number; optional):
    Image height, defaults to original image height adjusted to given
    width.

- placeholder (a list of or a singular dash component, string or number; optional):
    Customize placeholder content.

- radius (number; optional):
    Predefined border-radius value from theme.radius or number for
    border-radius in px.

- src (string; optional):
    Image src.

- style (boolean | number | string | dict | list; optional):
    Inline style.

- styles (boolean | number | string | dict | list; optional):
    Mantine styles API.

- sx (boolean | number | string | dict | list; optional):
    With sx you can add styles to component root element. If you need
    to customize styles of other elements within component use styles
    prop.

- width (string | number; optional):
    Image width, defaults to 100%, cannot exceed 100%.

- withPlaceholder (boolean; optional):
    Enable placeholder when image is loading and when image fails to
    load."""
    _children_props = ['placeholder', 'caption']
    _base_nodes = ['placeholder', 'caption', 'children']
    _namespace = 'dash_mantine_components'
    _type = 'Image'
    @_explicitize_args
    def __init__(self, src=Component.UNDEFINED, alt=Component.UNDEFINED, fit=Component.UNDEFINED, width=Component.UNDEFINED, height=Component.UNDEFINED, radius=Component.UNDEFINED, withPlaceholder=Component.UNDEFINED, placeholder=Component.UNDEFINED, caption=Component.UNDEFINED, className=Component.UNDEFINED, classNames=Component.UNDEFINED, style=Component.UNDEFINED, styles=Component.UNDEFINED, id=Component.UNDEFINED, unstyled=Component.UNDEFINED, sx=Component.UNDEFINED, m=Component.UNDEFINED, my=Component.UNDEFINED, mx=Component.UNDEFINED, mt=Component.UNDEFINED, mb=Component.UNDEFINED, ml=Component.UNDEFINED, mr=Component.UNDEFINED, p=Component.UNDEFINED, py=Component.UNDEFINED, px=Component.UNDEFINED, pt=Component.UNDEFINED, pb=Component.UNDEFINED, pl=Component.UNDEFINED, pr=Component.UNDEFINED, bg=Component.UNDEFINED, c=Component.UNDEFINED, opacity=Component.UNDEFINED, ff=Component.UNDEFINED, fz=Component.UNDEFINED, fw=Component.UNDEFINED, lts=Component.UNDEFINED, ta=Component.UNDEFINED, lh=Component.UNDEFINED, fs=Component.UNDEFINED, tt=Component.UNDEFINED, td=Component.UNDEFINED, w=Component.UNDEFINED, miw=Component.UNDEFINED, maw=Component.UNDEFINED, h=Component.UNDEFINED, mih=Component.UNDEFINED, mah=Component.UNDEFINED, bgsz=Component.UNDEFINED, bgp=Component.UNDEFINED, bgr=Component.UNDEFINED, pos=Component.UNDEFINED, top=Component.UNDEFINED, left=Component.UNDEFINED, bottom=Component.UNDEFINED, right=Component.UNDEFINED, inset=Component.UNDEFINED, display=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'alt', 'bg', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'caption', 'className', 'classNames', 'display', 'ff', 'fit', 'fs', 'fw', 'fz', 'h', 'height', 'inset', 'left', 'lh', 'lts', 'm', 'mah', 'maw', 'mb', 'mih', 'miw', 'ml', 'mr', 'mt', 'mx', 'my', 'opacity', 'p', 'pb', 'pl', 'placeholder', 'pos', 'pr', 'pt', 'px', 'py', 'radius', 'right', 'src', 'style', 'styles', 'sx', 'ta', 'td', 'top', 'tt', 'unstyled', 'w', 'width', 'withPlaceholder']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'alt', 'bg', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'caption', 'className', 'classNames', 'display', 'ff', 'fit', 'fs', 'fw', 'fz', 'h', 'height', 'inset', 'left', 'lh', 'lts', 'm', 'mah', 'maw', 'mb', 'mih', 'miw', 'ml', 'mr', 'mt', 'mx', 'my', 'opacity', 'p', 'pb', 'pl', 'placeholder', 'pos', 'pr', 'pt', 'px', 'py', 'radius', 'right', 'src', 'style', 'styles', 'sx', 'ta', 'td', 'top', 'tt', 'unstyled', 'w', 'width', 'withPlaceholder']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(Image, self).__init__(**args)
