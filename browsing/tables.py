import django_tables2 as tables
from django_tables2.utils import A
from tablets.models import Tablet, Sign, Glyph, TabletImage


class TabletTable(tables.Table):
    id = tables.Column(verbose_name="ID")
    title = tables.LinkColumn(
        "tablets:tablet_detail", args=[A("pk")], verbose_name="Tablet"
    )
    period = tables.Column(verbose_name="Period")
    place = tables.Column(verbose_name="Place")
    text_type = tables.Column(verbose_name="Text Type")
    nrglyphs = tables.Column(
        empty_values=(), orderable=False, verbose_name="Number of Glyphs"
    )

    def render_nrglyphs(self, value, record):
        glyphs = Glyph.objects.filter(tablet=record.id)
        return len(glyphs)

    class Meta:
        model = Tablet
        fields = ["title"]
        attrs = {"class": "table table-hover table-striped table-condensed"}


class SignTable(tables.Table):
    sign_name = tables.LinkColumn(
        "tablets:sign_detail", args=[A("pk")], verbose_name="Sign Name"
    )
    nrglyphs = tables.Column(
        empty_values=(), orderable=False, verbose_name="Number of Glyphs"
    )

    def render_nrglyphs(self, value, record):
        glyphs = Glyph.objects.filter(sign=record.id)
        return len(glyphs)

    class Meta:
        model = Sign
        exclude = ["image_1", "image_2"]
        attrs = {"class": "table table-hover table-striped table-condensed"}


class GlyphTable(tables.Table):
    identifier = tables.LinkColumn(
        "tablets:glyph_detail", args=[A("pk")], verbose_name="Glyph"
    )
    tablet = tables.LinkColumn(
        "tablets:tablet_detail", args=[A("tablet.pk")], verbose_name="Tablet"
    )
    sign = tables.LinkColumn(
        "tablets:sign_detail", args=[A("sign.pk")], verbose_name="Sign"
    )

    class Meta:
        model = Glyph
        exclude = ["id", "image", "note"]
        attrs = {"class": "table table-hover table-striped table-condensed"}


class CompareSignTable(tables.Table):
    identifier = tables.LinkColumn(
        "tablets:glyph_detail", args=[A("pk")], verbose_name="Glyph"
    )
    tablet = tables.LinkColumn(
        "tablets:tablet_detail", args=[A("tablet.pk")], verbose_name="Tablet"
    )
    sign = tables.LinkColumn(
        "tablets:sign_detail", args=[A("sign.pk")], verbose_name="Sign"
    )

    class Meta:
        model = Glyph
        exclude = ["id", "image", "note"]
        attrs = {"class": "table table-hover table-striped table-condensed"}


class TabletImageTable(tables.Table):
    id = tables.LinkColumn(
        "tablets:tabletimg_detail", args=[A("pk")], verbose_name="ID"
    )
    tablet = tables.LinkColumn(
        "tablets:tablet_detail", args=[A("tablet.pk")], verbose_name="Tablet"
    )

    class Meta:
        model = TabletImage
        exclude = ["comment"]
        attrs = {"class": "table table-hover table-striped table-condensed"}
