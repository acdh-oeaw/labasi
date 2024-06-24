from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset


class GenericFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(GenericFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = "genericFilterForm"
        self.form_method = "GET"
        self.add_input(Submit("Filter", "Filter"))


class TabletFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(TabletFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = "genericFilterForm"
        self.form_method = "GET"
        self.add_input(Submit("Filter", "Filter"))
        self.layout = Layout(
            Fieldset(
                "Basic search options",
                "text_reference",
                "region",
                "place",
                "scribe",
                "text_type",
                "period",
                "year",
                "date_not_before",
                "date_not_after",
                "babyloneian_time",
                css_id="basic_search_fields",
            ),
            Fieldset(
                "Advanced search options",
                "archive",
                "dossier",
                "cdli_no",
                "nabucco_no",
                "museum_no",
                "date_comment",
                "ductus",
                "content",
                "distinctive_protagonists",
                "bibliography",
                css_id="advanced_search_fields",
            ),
        )
