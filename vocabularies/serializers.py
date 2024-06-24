from rest_framework import serializers
from .models import *


class RegionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Region
        fields = "__all__"


class ArchiveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Archive
        fields = "__all__"


class DossierSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dossier
        fields = "__all__"


class ScribeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Scribe
        fields = "__all__"


class PeriodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Period
        fields = "__all__"


class TextTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TextType
        fields = "__all__"
