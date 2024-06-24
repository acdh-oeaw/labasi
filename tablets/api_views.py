from rest_framework import viewsets
from .models import Sign, Tablet, TabletImage, Glyph
from .serializers import (
    SignSerializer,
    TabletSerializer,
    TabletImageSerializer,
    GlyphSerializer,
)


class SignViewSet(viewsets.ModelViewSet):
    queryset = Sign.objects.all()
    serializer_class = SignSerializer
    depth = 2


class TabletViewSet(viewsets.ModelViewSet):
    queryset = Tablet.objects.all()
    serializer_class = TabletSerializer
    depth = 2


class TabletImageViewSet(viewsets.ModelViewSet):
    queryset = TabletImage.objects.all()
    serializer_class = TabletImageSerializer
    depth = 2


class GlyphViewSet(viewsets.ModelViewSet):
    queryset = Glyph.objects.all()
    serializer_class = GlyphSerializer
    depth = 2
