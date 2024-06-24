import django_filters
from tablets.models import Tablet, Sign, Glyph, TabletImage
from vocabularies.models import Region
from places.models import Place

django_filters.filters.LOOKUP_TYPES = [
    ("", "---------"),
    ("exact", "Is equal to"),
    ("iexact", "Is equal to (case insensitive)"),
    ("not_exact", "Is not equal to"),
    ("lt", "Lesser than/before"),
    ("gt", "Greater than/after"),
    ("gte", "Greater than or equal to"),
    ("lte", "Lesser than or equal to"),
    ("startswith", "Starts with"),
    ("endswith", "Ends with"),
    ("contains", "Contains"),
    ("icontains", "Contains (case insensitive)"),
    ("not_contains", "Does not contain"),
]


class TabletImageListFilter(django_filters.FilterSet):
    tablet__title = django_filters.CharFilter(
        lookup_expr="icontains", help_text="Filter by (part of the) tablets's name."
    )
    tablet = django_filters.ModelMultipleChoiceFilter(
        queryset=Tablet.objects.all(),
        label="Tablet",
        help_text="Filter by selecting one ore more Tablets.",
    )
    comment = django_filters.CharFilter(
        lookup_expr="icontains", help_text="Filter by (part of the) comments."
    )

    class Meta:
        model = TabletImage
        exclude = ["image"]


class TabletListFilter(django_filters.FilterSet):
    text_reference = django_filters.CharFilter(
        lookup_expr="icontains", label="Tablet", help_text=False
    )
    title = django_filters.CharFilter(lookup_expr="icontains", help_text=False)
    cdli_no = django_filters.CharFilter(
        lookup_expr="icontains", label="CDLI no.", help_text=False
    )
    nabucco_no = django_filters.CharFilter(
        lookup_expr="icontains", label="NABUCCO no.", help_text=False
    )
    museum_no = django_filters.CharFilter(
        lookup_expr="icontains", label="Museum no.", help_text=False
    )
    date_not_before = django_filters.NumberFilter(
        lookup_expr="lte", label="Date not before", help_text="Lesser than or equal to"
    )
    date_not_after = django_filters.NumberFilter(
        lookup_expr="gte", label="Date not after", help_text="Greater than or equal to"
    )
    date_comment = django_filters.CharFilter(lookup_expr="icontains", help_text=False)
    babyloneian_time = django_filters.CharFilter(
        lookup_expr="icontains", help_text=False, label="Babylonian time"
    )
    content = django_filters.CharFilter(lookup_expr="icontains", help_text=False)
    distinctive_protagonists = django_filters.CharFilter(
        lookup_expr="icontains", help_text=False
    )
    bibliography = django_filters.CharFilter(lookup_expr="icontains", help_text=False)

    class Meta:
        model = Tablet
        exclude = ["image"]


class SignListFilter(django_filters.FilterSet):
    sign_name = django_filters.CharFilter(lookup_expr="icontains", help_text=False)
    sign_name = django_filters.ModelMultipleChoiceFilter(
        queryset=Sign.objects.all(),
        label="Signs",
        help_text="Filter by selecting one ore more Signs.",
    )
    abz_number = django_filters.CharFilter(lookup_expr="icontains", help_text=False)
    meszl_number = django_filters.CharFilter(lookup_expr="icontains", help_text=False)

    class Meta:
        model = Sign
        exclude = ["image_1", "image_2"]


class GlyphListFilter(django_filters.FilterSet):
    identifier = django_filters.CharFilter(lookup_expr="icontains", help_text=False)
    tablet__title = django_filters.CharFilter(
        lookup_expr="icontains", help_text="Filter by (part of the) tablets's name."
    )
    sign__sign_name = django_filters.CharFilter(
        lookup_expr="icontains", help_text="Filter by (part of the) sign's name."
    )
    sign__sign_name = django_filters.CharFilter(
        lookup_expr="icontains", help_text="Filter by (part of the) sign's reading'."
    )
    tablet__date_not_before = django_filters.NumberFilter(
        lookup_expr="lte",
        label="Date not before (BC)",
        help_text="Lesser than or equal to",
    )
    tablet__date_not_after = django_filters.NumberFilter(
        lookup_expr="gte",
        label="Date not after (BC)",
        help_text="Greater than or equal to",
    )
    context = django_filters.CharFilter(
        lookup_expr="icontains", help_text="Filter by (part of the) glyphs's context'."
    )
    note = django_filters.CharFilter(
        lookup_expr="icontains", help_text="Filter by (part of the) glyphs's note'."
    )
    sign = django_filters.ModelMultipleChoiceFilter(
        queryset=Sign.objects.all(),
        label="Signs",
        help_text="Filter by selecting one ore more Signs.",
    )
    reading = django_filters.ModelMultipleChoiceFilter(
        queryset=Sign.objects.all(),
        label="Signs",
        help_text="Filter by selecting one ore more Readings.",
    )
    tablet__place = django_filters.ModelMultipleChoiceFilter(
        queryset=Place.objects.all(),
        label="Place",
        help_text="Filter by selecting one ore more Signs.",
    )
    tablet__region = django_filters.ModelMultipleChoiceFilter(
        queryset=Region.objects.all(),
        label="Region",
        help_text="Filter by selecting one ore more Signs.",
    )

    class Meta:
        model = Glyph
        exclude = ["tablet", "image"]


# filter by sign, returns glyphs
class CompareSignsListFilter(django_filters.FilterSet):
    sign1 = django_filters.ModelChoiceFilter(
        queryset=Sign.objects.all(),
        label="Signs1",
        name="sign__sign_name",
        help_text="Filter by selecting one ore more Signs.",
        method="custom_filter_sign1",
    )
    sign2 = django_filters.ModelChoiceFilter(
        queryset=Sign.objects.all(),
        label="Signs2",
        name="sign__sign_name",
        help_text="Filter by selecting one ore more Signs.",
        method="custom_filter_sign2",
    )
    sign__abz_number = django_filters.CharFilter(
        lookup_expr="icontains", help_text=False
    )
    sign__meszl_number = django_filters.CharFilter(
        lookup_expr="icontains", help_text=False
    )

    class Meta:
        model = Glyph
        fields = ["sign1", "sign2", "sign__abz_number", "sign__meszl_number"]

    def custom_filter_sign1(self, qs, name, value):
        if value:
            qs = Glyph.objects.filter(sign__sign_name=value)
        return qs

    def custom_filter_sign2(self, qs, name, value):
        if value:
            qs += Glyph.objects.filter(sign__sign_name=value)
        return qs
