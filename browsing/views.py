from django_tables2 import SingleTableView, RequestConfig
from tablets.models import Tablet, Sign, Glyph, TabletImage
from .filters import TabletListFilter, SignListFilter, GlyphListFilter, TabletImageListFilter
from .forms import GenericFilterFormHelper
from .tables import TabletTable, SignTable, GlyphTable, TabletImageTable


class GenericListView(SingleTableView):
    filter_class = None
    formhelper_class = None
    context_filter_name = 'filter'
    paginate_by = 25

    def get_queryset(self, **kwargs):
        qs = super(GenericListView, self).get_queryset()
        self.filter = self.filter_class(self.request.GET, queryset=qs)
        self.filter.form.helper = self.formhelper_class()
        return self.filter.qs

    def get_table(self, **kwargs):
        table = super(GenericListView, self).get_table()
        RequestConfig(self.request, paginate={
            'page': 1, 'per_page': self.paginate_by}).configure(table)
        return table

    def get_context_data(self, **kwargs):
        context = super(GenericListView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        return context


class TabletListView(GenericListView):
    model = Tablet
    table_class = TabletTable
    template_name = 'browsing/tablet_list_generic.html'
    filter_class = TabletListFilter
    formhelper_class = GenericFilterFormHelper


class SignListView(GenericListView):
    model = Sign
    table_class = SignTable
    template_name = 'browsing/sign_list_generic.html'
    filter_class = SignListFilter
    formhelper_class = GenericFilterFormHelper


class GlyphListView(GenericListView):
    model = Glyph
    table_class = GlyphTable
    template_name = 'browsing/glyph_list_generic.html'
    filter_class = GlyphListFilter
    formhelper_class = GenericFilterFormHelper


class TabletImageListView(GenericListView):
    model = TabletImage
    table_class = TabletImageTable
    template_name = 'browsing/tabletImage_list_generic.html'
    filter_class = TabletImageListFilter
    formhelper_class = GenericFilterFormHelper
