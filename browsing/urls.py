from django.urls import re_path
from . import views

app_name = "browsing"

urlpatterns = [
    re_path(r"tablets/$", views.TabletListView.as_view(), name="browse_tablets"),
    re_path(r"signs/$", views.SignListView.as_view(), name="browse_signs"),
    re_path(r"glyphs/$", views.GlyphListView.as_view(), name="browse_glyphs"),
    re_path(
        r"tabletimages/$",
        views.TabletImageListView.as_view(),
        name="browse_tabletimages",
    ),
    re_path(r"signs-compare/$", views.compare_signs, name="compare_signs"),
]
