from django.urls import re_path
from . import views

app_name = "tablets"

urlpatterns = [
    re_path(
        r"^detail/(?P<pk>[0-9]+)$",
        views.TabletDetailView.as_view(),
        name="tablet_detail",
    ),
    re_path(r"^detail/(?P<pk>[0-9]+)/xml$", views.tablet_to_tei, name="tablet_to_tei"),
    re_path(r"^create/$", views.create_tablet, name="tablet_create"),
    re_path(r"^edit/(?P<pk>[0-9]+)$", views.edit_tablet, name="tablet_edit"),
    re_path(
        r"^delete/(?P<pk>[0-9]+)$", views.TabletDelete.as_view(), name="tablet_delete"
    ),
    re_path(
        r"^sign/detail/(?P<pk>[0-9]+)$",
        views.SignDetailView.as_view(),
        name="sign_detail",
    ),
    re_path(r"^sign/create/$", views.create_sign, name="sign_create"),
    re_path(r"^sign/edit/(?P<pk>[0-9]+)$", views.edit_sign, name="sign_edit"),
    re_path(
        r"^sign/delete/(?P<pk>[0-9]+)$", views.SignDelete.as_view(), name="sign_delete"
    ),
    re_path(
        r"^glyph/detail/(?P<pk>[0-9]+)$",
        views.GlyphDetailView.as_view(),
        name="glyph_detail",
    ),
    re_path(r"^glyph/create/$", views.create_glyph, name="glyph_create"),
    re_path(r"^glyph/edit/(?P<pk>[0-9]+)$", views.edit_glyph, name="glyph_edit"),
    re_path(
        r"^glyph/delete/(?P<pk>[0-9]+)$",
        views.GlyphDelete.as_view(),
        name="glyph_delete",
    ),
    re_path(
        r"^tabletimg/detail/(?P<pk>[0-9]+)$",
        views.TabletImageDetailView.as_view(),
        name="tabletimg_detail",
    ),
    re_path(r"^tabletimg/create/$", views.create_tabletImg, name="tabletimg_create"),
    re_path(
        r"^tabletimg/edit/(?P<pk>[0-9]+)$", views.edit_tabletImg, name="tabletimg_edit"
    ),
    re_path(
        r"^tabletimage/delete/(?P<pk>[0-9]+)$",
        views.TabletImageDelete.as_view(),
        name="tabletimage_delete",
    ),
    re_path(
        r"^tabletimage/cut/(?P<pk>[0-9]+)$", views.cut_tabletImg, name="tabletimage_cut"
    ),
]
