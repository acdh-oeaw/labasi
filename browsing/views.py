from django_tables2 import SingleTableView, RequestConfig
from tablets.models import Tablet, Sign, Glyph, TabletImage
from .filters import (
    GlyphListFilter,
    SignListFilter,
    TabletImageListFilter,
    TabletListFilter,
)
from .forms import GenericFilterFormHelper, TabletFilterFormHelper
from .tables import GlyphTable, SignTable, TabletImageTable, TabletTable
from django.shortcuts import render
from vocabularies.models import Region, Period


class GenericListView(SingleTableView):
    filter_class = None
    formhelper_class = None
    context_filter_name = "filter"
    paginate_by = 25

    def get_queryset(self, **kwargs):
        qs = super(GenericListView, self).get_queryset()
        self.filter = self.filter_class(self.request.GET, queryset=qs)
        self.filter.form.helper = self.formhelper_class()
        return self.filter.qs

    def get_table(self, **kwargs):
        table = super(GenericListView, self).get_table()
        RequestConfig(
            self.request, paginate={"page": 1, "per_page": self.paginate_by}
        ).configure(table)
        return table

    def get_context_data(self, **kwargs):
        context = super(GenericListView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        return context


class TabletListView(GenericListView):
    model = Tablet
    table_class = TabletTable
    template_name = "browsing/tablet_list_generic.html"
    filter_class = TabletListFilter
    formhelper_class = TabletFilterFormHelper


class SignListView(GenericListView):
    model = Sign
    table_class = SignTable
    template_name = "browsing/sign_list_generic.html"
    filter_class = SignListFilter
    formhelper_class = GenericFilterFormHelper


class GlyphListView(GenericListView):
    model = Glyph
    table_class = GlyphTable
    template_name = "browsing/glyph_list_generic.html"
    filter_class = GlyphListFilter
    formhelper_class = GenericFilterFormHelper


def compare_signs(request):
    context = {}
    if "sign_first" and "sign_second" in request.GET:
        sign_first_string = request.GET.get("sign_first", "")
        sign_second_string = request.GET.get("sign_second", "")
        sign_first_results = Glyph.objects.filter(sign__sign_name=sign_first_string)
        sign_second_results = Glyph.objects.filter(sign__sign_name=sign_second_string)
        sign_first_results_count = sign_first_results.count()
        sign_second_results_count = sign_second_results.count()
        sign_obj_f = Sign.objects.filter(sign_name=sign_first_string)
        sign_obj_s = Sign.objects.filter(sign_name=sign_second_string)
    else:
        sign_first_string = ""
        sign_first_results = None
        sign_first_results_count = None
        sign_second_string = ""
        sign_second_results = None
        sign_second_results_count = None
        sign_obj_f = None
        sign_obj_s = None
    context["sign_first_string"] = sign_first_string
    context["sign_first_results"] = sign_first_results
    context["sign_first_results_count"] = sign_first_results_count
    context["sign_second_string"] = sign_second_string
    context["sign_second_results"] = sign_second_results
    context["sign_second_results_count"] = sign_second_results_count
    signs = Sign.objects.all()
    context["signs"] = signs
    context["sign_obj_f"] = sign_obj_f
    context["sign_obj_s"] = sign_obj_s
    context["region_list"] = Region.objects.exclude(name="")
    context["period_list"] = (
        Period.objects.values_list("name", flat=True).distinct().exclude(name="")
    )
    return render(request, "browsing/compare_sign_list_generic.html", context)


class TabletImageListView(GenericListView):
    model = TabletImage
    table_class = TabletImageTable
    template_name = "browsing/tabletimage_list_generic.html"
    filter_class = TabletImageListFilter
    formhelper_class = GenericFilterFormHelper
