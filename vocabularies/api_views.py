from rest_framework import viewsets
from .models import *
from .serializers import *


class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    depth = 2


class ArchiveViewSet(viewsets.ModelViewSet):
    queryset = Archive.objects.all()
    serializer_class = ArchiveSerializer
    depth = 2


class DossierViewSet(viewsets.ModelViewSet):
    queryset = Dossier.objects.all()
    serializer_class = DossierSerializer
    depth = 2


class ScribeViewSet(viewsets.ModelViewSet):
    queryset = Scribe.objects.all()
    serializer_class = ScribeSerializer
    depth = 2


class PeriodViewSet(viewsets.ModelViewSet):
    queryset = Period.objects.all()
    serializer_class = PeriodSerializer
    depth = 2


class TextTypeViewSet(viewsets.ModelViewSet):
    queryset = TextType.objects.all()
    serializer_class = TextTypeSerializer
    depth = 2
