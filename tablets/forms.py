from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from .models import Tablet, Glyph, TabletImage, Sign


class CutForm(forms.ModelForm):
    class Meta:
        model = Glyph
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(CutForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            "sign",
            "reading",
            "context",
            "note",
            Field("identifier", type="hidden"),
            Field("tablet", type="hidden"),
            Field("image", type="hidden"),
        )


class TabletForm(forms.ModelForm):
    class Meta:
        model = Tablet
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(TabletForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "save"))


class GlyphForm(forms.ModelForm):
    class Meta:
        model = Glyph
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(GlyphForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "save"))


class TabletImageForm(forms.ModelForm):
    class Meta:
        model = TabletImage
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(TabletImageForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "save"))


class SignForm(forms.ModelForm):
    class Meta:
        model = Sign
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(SignForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "save"))
