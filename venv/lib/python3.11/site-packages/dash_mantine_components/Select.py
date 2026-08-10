# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Select(Component):
    """A Select component.
Custom searchable select. For more information, see: https://mantine.dev/core/select/

Keyword arguments:

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- allowDeselect (boolean; optional):
    Allow deselecting items on click.

- className (string; optional):
    Often used with CSS to style elements with common properties.

- classNames (dict; optional):
    add class names to Mantine components.

- clearable (boolean; optional):
    Allow to clear item.

- creatable (boolean; optional):
    Allow creatable option.

- data (list of strings; optional):
    Select data used to renderer items in dropdown.

- debounce (number; optional):
    Debounce time.

- description (a list of or a singular dash component, string or number; optional):
    Input description, displayed after label.

- disabled (boolean; optional):
    Whether the input is disabled   Disabled input state.

- dropdownPosition (a value equal to: 'bottom', 'top', 'flip'; optional):
    Dropdown positioning behavior.

- error (a list of or a singular dash component, string or number; optional):
    Displays error message after input.

- filterDataOnExactSearchMatch (boolean; optional):
    Should data be filtered when search value exactly matches selected
    item.

- icon (a list of or a singular dash component, string or number; optional):
    Adds icon on the left side of input.

- iconWidth (number; optional):
    Width of icon section in px.

- initiallyOpened (boolean; optional):
    Initial dropdown opened state.

- inputWrapperOrder (list of a value equal to: 'label', 'description', 'error', 'input's; optional):
    Controls order of the Input.Wrapper elements.

- label (a list of or a singular dash component, string or number; optional):
    Input label, displayed before input.

- limit (number; optional):
    Limit amount of items displayed at a time for searchable select.

- maxDropdownHeight (number; optional):
    Maximum dropdown height in px.

- name (string; optional):
    Name prop.

- nothingFound (a list of or a singular dash component, string or number; optional):
    Nothing found label.

- persisted_props (list of strings; default ["value"]):
    Properties whose user interactions will persist after refreshing
    the component or the page. Since only `value` is allowed this prop
    can normally be ignored.

- persistence (string | number; optional):
    Used to allow user interactions in this component to be persisted
    when the component - or the page - is refreshed. If `persisted` is
    truthy and hasn't changed from its previous value, a `value` that
    the user has changed while using the app will keep that change, as
    long as the new `value` also matches what was given originally.
    Used in conjunction with `persistence_type`.

- persistence_type (a value equal to: 'local', 'session', 'memory'; default 'local'):
    Where persisted user changes will be stored: memory: only kept in
    memory, reset on page refresh. local: window.localStorage, data is
    kept after the browser quit. session: window.sessionStorage, data
    is cleared once the browser quit.

- placeholder (string; optional):
    Placeholder.

- radius (number; optional):
    Input border-radius from theme or number to set border-radius in
    px.

- required (boolean; optional):
    Adds required attribute to the input and red asterisk on the right
    side of label   Sets required on input element.

- rightSection (a list of or a singular dash component, string or number; optional):
    Right section of input, similar to icon but on the right.

- rightSectionWidth (number; optional):
    Width of right section, is used to calculate input padding-right.

- searchValue (string; optional):
    Controlled search input value.

- searchable (boolean; optional):
    Enable items searching.

- selectOnBlur (boolean; optional):
    Select highlighted item on blur.

- shadow (boolean | number | string | dict | list; optional):
    Dropdown shadow from theme or any value to set box-shadow.

- size (a value equal to: 'xs', 'sm', 'md', 'lg', 'xl'; optional):
    Input size.

- style (boolean | number | string | dict | list; optional):
    Inline style.

- styles (boolean | number | string | dict | list; optional):
    Mantine styles API.

- switchDirectionOnFlip (boolean; optional):
    Whether to switch item order and keyboard navigation on dropdown
    position flip.

- sx (boolean | number | string | dict | list; optional):
    With sx you can add styles to component root element. If you need
    to customize styles of other elements within component use styles
    prop.

- transition (a value equal to: 'fade', 'skew-up', 'skew-down', 'rotate-right', 'rotate-left', 'slide-down', 'slide-up', 'slide-right', 'slide-left', 'scale-y', 'scale-x', 'scale', 'pop', 'pop-top-left', 'pop-top-right', 'pop-bottom-left', 'pop-bottom-right'; optional):
    Dropdown body appear/disappear transition.

- transitionDuration (number; optional):
    Dropdown body transition duration.

- transitionTimingFunction (string; optional):
    Dropdown body transition timing function, defaults to
    theme.transitionTimingFunction.

- value (string; optional):
    Controlled input value.

- variant (a value equal to: 'default', 'filled', 'unstyled'; optional):
    Defines input appearance, defaults to default in light color
    scheme and filled in dark.

- withAsterisk (boolean; optional):
    Determines whether required asterisk should be rendered, overrides
    required prop, does not add required attribute to the input.

- zIndex (number; optional):
    Dropdown z-index."""
    _children_props = ['nothingFound', 'label', 'description', 'error', 'icon', 'rightSection']
    _base_nodes = ['nothingFound', 'label', 'description', 'error', 'icon', 'rightSection', 'children']
    _namespace = 'dash_mantine_components'
    _type = 'Select'
    @_explicitize_args
    def __init__(self, allowDeselect=Component.UNDEFINED, filterDataOnExactSearchMatch=Component.UNDEFINED, value=Component.UNDEFINED, persistence=Component.UNDEFINED, persisted_props=Component.UNDEFINED, persistence_type=Component.UNDEFINED, data=Component.UNDEFINED, size=Component.UNDEFINED, maxDropdownHeight=Component.UNDEFINED, selectOnBlur=Component.UNDEFINED, transition=Component.UNDEFINED, transitionDuration=Component.UNDEFINED, transitionTimingFunction=Component.UNDEFINED, shadow=Component.UNDEFINED, initiallyOpened=Component.UNDEFINED, limit=Component.UNDEFINED, nothingFound=Component.UNDEFINED, zIndex=Component.UNDEFINED, searchValue=Component.UNDEFINED, dropdownPosition=Component.UNDEFINED, switchDirectionOnFlip=Component.UNDEFINED, clearable=Component.UNDEFINED, creatable=Component.UNDEFINED, searchable=Component.UNDEFINED, disabled=Component.UNDEFINED, label=Component.UNDEFINED, description=Component.UNDEFINED, error=Component.UNDEFINED, required=Component.UNDEFINED, withAsterisk=Component.UNDEFINED, inputWrapperOrder=Component.UNDEFINED, icon=Component.UNDEFINED, iconWidth=Component.UNDEFINED, rightSection=Component.UNDEFINED, rightSectionWidth=Component.UNDEFINED, radius=Component.UNDEFINED, variant=Component.UNDEFINED, placeholder=Component.UNDEFINED, name=Component.UNDEFINED, debounce=Component.UNDEFINED, className=Component.UNDEFINED, classNames=Component.UNDEFINED, style=Component.UNDEFINED, styles=Component.UNDEFINED, id=Component.UNDEFINED, unstyled=Component.UNDEFINED, sx=Component.UNDEFINED, m=Component.UNDEFINED, my=Component.UNDEFINED, mx=Component.UNDEFINED, mt=Component.UNDEFINED, mb=Component.UNDEFINED, ml=Component.UNDEFINED, mr=Component.UNDEFINED, p=Component.UNDEFINED, py=Component.UNDEFINED, px=Component.UNDEFINED, pt=Component.UNDEFINED, pb=Component.UNDEFINED, pl=Component.UNDEFINED, pr=Component.UNDEFINED, bg=Component.UNDEFINED, c=Component.UNDEFINED, opacity=Component.UNDEFINED, ff=Component.UNDEFINED, fz=Component.UNDEFINED, fw=Component.UNDEFINED, lts=Component.UNDEFINED, ta=Component.UNDEFINED, lh=Component.UNDEFINED, fs=Component.UNDEFINED, tt=Component.UNDEFINED, td=Component.UNDEFINED, w=Component.UNDEFINED, miw=Component.UNDEFINED, maw=Component.UNDEFINED, h=Component.UNDEFINED, mih=Component.UNDEFINED, mah=Component.UNDEFINED, bgsz=Component.UNDEFINED, bgp=Component.UNDEFINED, bgr=Component.UNDEFINED, pos=Component.UNDEFINED, top=Component.UNDEFINED, left=Component.UNDEFINED, bottom=Component.UNDEFINED, right=Component.UNDEFINED, inset=Component.UNDEFINED, display=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'allowDeselect', 'bg', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'clearable', 'creatable', 'data', 'debounce', 'description', 'disabled', 'display', 'dropdownPosition', 'error', 'ff', 'filterDataOnExactSearchMatch', 'fs', 'fw', 'fz', 'h', 'icon', 'iconWidth', 'initiallyOpened', 'inputWrapperOrder', 'inset', 'label', 'left', 'lh', 'limit', 'lts', 'm', 'mah', 'maw', 'maxDropdownHeight', 'mb', 'mih', 'miw', 'ml', 'mr', 'mt', 'mx', 'my', 'name', 'nothingFound', 'opacity', 'p', 'pb', 'persisted_props', 'persistence', 'persistence_type', 'pl', 'placeholder', 'pos', 'pr', 'pt', 'px', 'py', 'radius', 'required', 'right', 'rightSection', 'rightSectionWidth', 'searchValue', 'searchable', 'selectOnBlur', 'shadow', 'size', 'style', 'styles', 'switchDirectionOnFlip', 'sx', 'ta', 'td', 'top', 'transition', 'transitionDuration', 'transitionTimingFunction', 'tt', 'unstyled', 'value', 'variant', 'w', 'withAsterisk', 'zIndex']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'allowDeselect', 'bg', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'clearable', 'creatable', 'data', 'debounce', 'description', 'disabled', 'display', 'dropdownPosition', 'error', 'ff', 'filterDataOnExactSearchMatch', 'fs', 'fw', 'fz', 'h', 'icon', 'iconWidth', 'initiallyOpened', 'inputWrapperOrder', 'inset', 'label', 'left', 'lh', 'limit', 'lts', 'm', 'mah', 'maw', 'maxDropdownHeight', 'mb', 'mih', 'miw', 'ml', 'mr', 'mt', 'mx', 'my', 'name', 'nothingFound', 'opacity', 'p', 'pb', 'persisted_props', 'persistence', 'persistence_type', 'pl', 'placeholder', 'pos', 'pr', 'pt', 'px', 'py', 'radius', 'required', 'right', 'rightSection', 'rightSectionWidth', 'searchValue', 'searchable', 'selectOnBlur', 'shadow', 'size', 'style', 'styles', 'switchDirectionOnFlip', 'sx', 'ta', 'td', 'top', 'transition', 'transitionDuration', 'transitionTimingFunction', 'tt', 'unstyled', 'value', 'variant', 'w', 'withAsterisk', 'zIndex']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(Select, self).__init__(**args)
