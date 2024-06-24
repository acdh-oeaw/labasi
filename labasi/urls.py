# import autocomplete_light.shortcuts as al
# al.autodiscover()

from django.urls import include, re_path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from tablets.views import protected_serve

from rest_framework import routers
from vocabularies.api_views import (
    RegionViewSet,
    ArchiveViewSet,
    DossierViewSet,
    ScribeViewSet,
    PeriodViewSet,
    TextTypeViewSet,
)

from tablets.api_views import GlyphViewSet, TabletViewSet, SignViewSet
from places.api_views import PlaceViewSet
from labels.api_views import LabelViewSet


router = routers.DefaultRouter()
router.register(r"places", PlaceViewSet)
router.register(r"labels", LabelViewSet)
router.register(r"regions", RegionViewSet)
router.register(r"archives", ArchiveViewSet)
router.register(r"dossiers", DossierViewSet)
router.register(r"scribes", ScribeViewSet)
router.register(r"periods", PeriodViewSet)
router.register(r"texttypes", TextTypeViewSet)
router.register(r"signs", SignViewSet)
router.register(r"tablets", TabletViewSet)
# router.register(r'tabletimages', TabletImageViewSet)
router.register(r"glyphs", GlyphViewSet)

urlpatterns = [
    re_path(r"^admin/", admin.site.urls),
    re_path(r"^data/api/", include(router.urls)),
    re_path(
        r"^data/api-auth/", include("rest_framework.urls", namespace="rest_framework")
    ),
    re_path(r"^", include("webpage.urls", namespace="webpage")),
    re_path(
        r"^media/tablet_img/(?P<pic>.*)$", protected_serve, name="protected_server"
    ),
    re_path(r"places/", include("places.urls", namespace="places")),
    re_path(r"labels/", include("labels.urls", namespace="labels")),
    re_path(r"browsing/", include("browsing.urls", namespace="browsing")),
    re_path(r"tablets/", include("tablets.urls", namespace="tablets")),
    re_path(r"charts/", include("charts.urls", namespace="charts")),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
