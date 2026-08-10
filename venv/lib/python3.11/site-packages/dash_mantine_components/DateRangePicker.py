# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DateRangePicker(Component):
    """A DateRangePicker component.
Capture date input from user. For more information, see: https://mantine.dev/dates/date-picker/

Keyword arguments:

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- allowLevelChange (boolean; optional):
    Allow to change level (date - month - year).

- allowSingleDateInRange (boolean; optional):
    Allow one date to be selected as range.

- amountOfMonths (number; optional):
    Amount of months.

- className (string; optional):
    Often used with CSS to style elements with common properties.

- classNames (dict; optional):
    add class names to Mantine components.

- clearButtonLabel (string; optional):
    aria-label for clear button.

- clearButtonTabIndex (a value equal to: 0, -1; optional):
    Set the clear button tab index to disabled or default after input
    field.

- clearable (boolean; optional):
    Allow to clear value.

- clickOutsideEvents (list of strings; optional):
    Events that should trigger outside clicks.

- closeCalendarOnChange (boolean; optional):
    Set to False to force dropdown to stay open after date was
    selected.

- debounce (number; optional):
    Debounce time.

- description (a list of or a singular dash component, string or number; optional):
    Input description, displayed after label.

- disableOutsideEvents (boolean; optional):
    When True dates that are outside of given month cannot be clicked
    or focused.

- disabled (boolean; optional):
    Disabled input state.

- disabledDates (list of strings; optional):
    Specifies additional days between min_date_allowed and
    max_date_allowed that should be disabled.

- dropdownPosition (a value equal to: 'bottom-start', 'top-start', 'flip'; optional):
    Dropdown positioning behavior.

- dropdownType (a value equal to: 'popover', 'modal'; optional):
    Where to show calendar in modal or popover.

- error (a list of or a singular dash component, string or number; optional):
    Displays error message after input.

- firstDayOfWeek (a value equal to: 'sunday', 'monday'; optional):
    Set first day of the week.

- fixOnBlur (boolean; optional):
    call onChange with last valid value onBlur.

- focusable (boolean; optional):
    Should focusable days have tabIndex={0}?.

- fullWidth (boolean; optional):
    Set to True to make calendar take 100% of container width.

- hideOutsideDates (boolean; optional):
    Remove outside dates.

- hideWeekdays (boolean; optional):
    Set to False to remove weekdays row.

- icon (a list of or a singular dash component, string or number; optional):
    Adds icon on the left side of input.

- iconWidth (number; optional):
    Width of icon section in px.

- initialLevel (a value equal to: 'date', 'month', 'year'; optional):
    Initial date selection level.

- initialMonth (string; optional):
    Initial month for uncontrolled calendar.

- initiallyOpened (boolean; optional):
    Control initial dropdown opened state.

- inputFormat (string; optional):
    dayjs input format.

- inputWrapperOrder (list of a value equal to: 'label', 'description', 'error', 'input's; optional):
    Controls order of the Input.Wrapper elements.

- label (a list of or a singular dash component, string or number; optional):
    Input label, displayed before input.

- labelSeparator (string; optional):
    Separator between dates.

- locale (string; optional):
    Locale used for labels formatting, defaults to theme.datesLocale.

- maxDate (string; optional):
    Maximum possible date.

- minDate (string; optional):
    Minimum possible date.

- modalZIndex (number; optional):
    Modal z-index.

- name (string; optional):
    Name prop.

- nextDecadeLabel (string; optional):
    Next decade control aria-label.

- nextMonthLabel (string; optional):
    Next month control aria-label.

- nextYearLabel (string; optional):
    Next year control aria-label.

- openDropdownOnClear (boolean; optional):
    Set to True to open dropdown on clear.

- paginateBy (number; optional):
    Paginate by amount of months.

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

- preventFocus (boolean; optional):
    Prevent focusing upon clicking.

- previousDecadeLabel (string; optional):
    Previous decade control aria-label.

- previousMonthLabel (string; optional):
    Previous month control aria-label.

- previousYearLabel (string; optional):
    Previous year control aria-label.

- radius (number; optional):
    Input border-radius from theme or number to set border-radius in
    px.

- required (boolean; optional):
    Sets required on input element   Adds required attribute to the
    input and red asterisk on the right side of label.

- rightSection (a list of or a singular dash component, string or number; optional):
    Right section of input, similar to icon but on the right.

- rightSectionWidth (number; optional):
    Width of right section, is used to calculate input padding-right.

- shadow (a value equal to: 'xs', 'sm', 'md', 'lg', 'xl'; optional):
    Dropdown shadow from theme or css value for custom box-shadow.

- size (a value equal to: 'xs', 'sm', 'md', 'lg', 'xl'; optional):
    Input size.

- style (boolean | number | string | dict | list; optional):
    Inline style.

- styles (boolean | number | string | dict | list; optional):
    Mantine styles API.

- sx (boolean | number | string | dict | list; optional):
    With sx you can add styles to component root element. If you need
    to customize styles of other elements within component use styles
    prop.

- transition (a value equal to: 'fade', 'skew-up', 'skew-down', 'rotate-right', 'rotate-left', 'slide-down', 'slide-up', 'slide-right', 'slide-left', 'scale-y', 'scale-x', 'scale', 'pop', 'pop-top-left', 'pop-top-right', 'pop-bottom-left', 'pop-bottom-right'; optional):
    Dropdown appear/disappear transition.

- transitionDuration (number; optional):
    Dropdown appear/disappear transition duration.

- transitionTimingFunction (string; optional):
    Dropdown appear/disappear transition timing function, defaults to
    theme.transitionTimingFunction.

- value (boolean | number | string | dict | list; optional):
    Selected date, required with controlled input.

- variant (a value equal to: 'unstyled', 'default', 'filled'; optional):
    Defines input appearance, defaults to default in light color
    scheme and filled in dark.

- weekendDays (list of numbers; optional):
    Indices of weekend days.

- withAsterisk (boolean; optional):
    Determines whether required asterisk should be rendered, overrides
    required prop, does not add required attribute to the input.

- zIndex (number; optional):
    Dropdown zIndex."""
    _children_props = ['icon', 'rightSection', 'label', 'description', 'error']
    _base_nodes = ['icon', 'rightSection', 'label', 'description', 'error', 'children']
    _namespace = 'dash_mantine_components'
    _type = 'DateRangePicker'
    @_explicitize_args
    def __init__(self, value=Component.UNDEFINED, allowSingleDateInRange=Component.UNDEFINED, labelSeparator=Component.UNDEFINED, className=Component.UNDEFINED, classNames=Component.UNDEFINED, style=Component.UNDEFINED, styles=Component.UNDEFINED, id=Component.UNDEFINED, unstyled=Component.UNDEFINED, sx=Component.UNDEFINED, m=Component.UNDEFINED, my=Component.UNDEFINED, mx=Component.UNDEFINED, mt=Component.UNDEFINED, mb=Component.UNDEFINED, ml=Component.UNDEFINED, mr=Component.UNDEFINED, p=Component.UNDEFINED, py=Component.UNDEFINED, px=Component.UNDEFINED, pt=Component.UNDEFINED, pb=Component.UNDEFINED, pl=Component.UNDEFINED, pr=Component.UNDEFINED, bg=Component.UNDEFINED, c=Component.UNDEFINED, opacity=Component.UNDEFINED, ff=Component.UNDEFINED, fz=Component.UNDEFINED, fw=Component.UNDEFINED, lts=Component.UNDEFINED, ta=Component.UNDEFINED, lh=Component.UNDEFINED, fs=Component.UNDEFINED, tt=Component.UNDEFINED, td=Component.UNDEFINED, w=Component.UNDEFINED, miw=Component.UNDEFINED, maw=Component.UNDEFINED, h=Component.UNDEFINED, mih=Component.UNDEFINED, mah=Component.UNDEFINED, bgsz=Component.UNDEFINED, bgp=Component.UNDEFINED, bgr=Component.UNDEFINED, pos=Component.UNDEFINED, top=Component.UNDEFINED, left=Component.UNDEFINED, bottom=Component.UNDEFINED, right=Component.UNDEFINED, inset=Component.UNDEFINED, display=Component.UNDEFINED, persistence=Component.UNDEFINED, persisted_props=Component.UNDEFINED, persistence_type=Component.UNDEFINED, transition=Component.UNDEFINED, transitionDuration=Component.UNDEFINED, transitionTimingFunction=Component.UNDEFINED, shadow=Component.UNDEFINED, size=Component.UNDEFINED, dropdownType=Component.UNDEFINED, dropdownPosition=Component.UNDEFINED, clearable=Component.UNDEFINED, zIndex=Component.UNDEFINED, fixOnBlur=Component.UNDEFINED, clickOutsideEvents=Component.UNDEFINED, modalZIndex=Component.UNDEFINED, clearButtonTabIndex=Component.UNDEFINED, amountOfMonths=Component.UNDEFINED, paginateBy=Component.UNDEFINED, allowLevelChange=Component.UNDEFINED, initialLevel=Component.UNDEFINED, disabledDates=Component.UNDEFINED, disableOutsideEvents=Component.UNDEFINED, fullWidth=Component.UNDEFINED, preventFocus=Component.UNDEFINED, focusable=Component.UNDEFINED, maxDate=Component.UNDEFINED, minDate=Component.UNDEFINED, hideWeekdays=Component.UNDEFINED, hideOutsideDates=Component.UNDEFINED, weekendDays=Component.UNDEFINED, firstDayOfWeek=Component.UNDEFINED, closeCalendarOnChange=Component.UNDEFINED, openDropdownOnClear=Component.UNDEFINED, inputFormat=Component.UNDEFINED, initiallyOpened=Component.UNDEFINED, initialMonth=Component.UNDEFINED, locale=Component.UNDEFINED, clearButtonLabel=Component.UNDEFINED, nextMonthLabel=Component.UNDEFINED, previousMonthLabel=Component.UNDEFINED, nextYearLabel=Component.UNDEFINED, previousYearLabel=Component.UNDEFINED, nextDecadeLabel=Component.UNDEFINED, previousDecadeLabel=Component.UNDEFINED, icon=Component.UNDEFINED, iconWidth=Component.UNDEFINED, rightSection=Component.UNDEFINED, rightSectionWidth=Component.UNDEFINED, required=Component.UNDEFINED, radius=Component.UNDEFINED, variant=Component.UNDEFINED, disabled=Component.UNDEFINED, placeholder=Component.UNDEFINED, name=Component.UNDEFINED, debounce=Component.UNDEFINED, label=Component.UNDEFINED, description=Component.UNDEFINED, error=Component.UNDEFINED, withAsterisk=Component.UNDEFINED, inputWrapperOrder=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'allowLevelChange', 'allowSingleDateInRange', 'amountOfMonths', 'bg', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'clearButtonLabel', 'clearButtonTabIndex', 'clearable', 'clickOutsideEvents', 'closeCalendarOnChange', 'debounce', 'description', 'disableOutsideEvents', 'disabled', 'disabledDates', 'display', 'dropdownPosition', 'dropdownType', 'error', 'ff', 'firstDayOfWeek', 'fixOnBlur', 'focusable', 'fs', 'fullWidth', 'fw', 'fz', 'h', 'hideOutsideDates', 'hideWeekdays', 'icon', 'iconWidth', 'initialLevel', 'initialMonth', 'initiallyOpened', 'inputFormat', 'inputWrapperOrder', 'inset', 'label', 'labelSeparator', 'left', 'lh', 'locale', 'lts', 'm', 'mah', 'maw', 'maxDate', 'mb', 'mih', 'minDate', 'miw', 'ml', 'modalZIndex', 'mr', 'mt', 'mx', 'my', 'name', 'nextDecadeLabel', 'nextMonthLabel', 'nextYearLabel', 'opacity', 'openDropdownOnClear', 'p', 'paginateBy', 'pb', 'persisted_props', 'persistence', 'persistence_type', 'pl', 'placeholder', 'pos', 'pr', 'preventFocus', 'previousDecadeLabel', 'previousMonthLabel', 'previousYearLabel', 'pt', 'px', 'py', 'radius', 'required', 'right', 'rightSection', 'rightSectionWidth', 'shadow', 'size', 'style', 'styles', 'sx', 'ta', 'td', 'top', 'transition', 'transitionDuration', 'transitionTimingFunction', 'tt', 'unstyled', 'value', 'variant', 'w', 'weekendDays', 'withAsterisk', 'zIndex']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'allowLevelChange', 'allowSingleDateInRange', 'amountOfMonths', 'bg', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'clearButtonLabel', 'clearButtonTabIndex', 'clearable', 'clickOutsideEvents', 'closeCalendarOnChange', 'debounce', 'description', 'disableOutsideEvents', 'disabled', 'disabledDates', 'display', 'dropdownPosition', 'dropdownType', 'error', 'ff', 'firstDayOfWeek', 'fixOnBlur', 'focusable', 'fs', 'fullWidth', 'fw', 'fz', 'h', 'hideOutsideDates', 'hideWeekdays', 'icon', 'iconWidth', 'initialLevel', 'initialMonth', 'initiallyOpened', 'inputFormat', 'inputWrapperOrder', 'inset', 'label', 'labelSeparator', 'left', 'lh', 'locale', 'lts', 'm', 'mah', 'maw', 'maxDate', 'mb', 'mih', 'minDate', 'miw', 'ml', 'modalZIndex', 'mr', 'mt', 'mx', 'my', 'name', 'nextDecadeLabel', 'nextMonthLabel', 'nextYearLabel', 'opacity', 'openDropdownOnClear', 'p', 'paginateBy', 'pb', 'persisted_props', 'persistence', 'persistence_type', 'pl', 'placeholder', 'pos', 'pr', 'preventFocus', 'previousDecadeLabel', 'previousMonthLabel', 'previousYearLabel', 'pt', 'px', 'py', 'radius', 'required', 'right', 'rightSection', 'rightSectionWidth', 'shadow', 'size', 'style', 'styles', 'sx', 'ta', 'td', 'top', 'transition', 'transitionDuration', 'transitionTimingFunction', 'tt', 'unstyled', 'value', 'variant', 'w', 'weekendDays', 'withAsterisk', 'zIndex']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(DateRangePicker, self).__init__(**args)
