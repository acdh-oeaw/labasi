from django.urls import re_path
from . import views

app_name = "charts"

urlpatterns = [
    re_path(r"^barcharts/$", views.barcharts_view, name="bar_charts"),
    re_path(r"^testjson/$", views.test_json, name="test_json"),
    re_path(
        r"^tablets_per_region/$", views.tablets_per_region, name="tablets_per_region"
    ),
    re_path(
        r"^tablets_per_scribe/$", views.tablets_per_scribe, name="tablets_per_scribe"
    ),
    re_path(
        r"^tablets_per_period/$", views.tablets_per_period, name="tablets_per_period"
    ),
    re_path(r"^glyphs_per_sign/$", views.glyphs_per_sign, name="glyphs_per_sign"),
]
