from rest_framework import serializers
from vocabularies.serializers import *
from places.serializers import *
from .models import *


class SignSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sign
        fields = "__all__"


class TabletSerializer(serializers.HyperlinkedModelSerializer):
    archive = ArchiveSerializer()
    place = PlaceSerializer()
    scribe = ScribeSerializer()
    period = PeriodSerializer()
    text_type = TextTypeSerializer()

    class Meta:
        model = Tablet
        fields = "__all__"


class TabletImageSerializer(serializers.HyperlinkedModelSerializer):
    tablet = TabletSerializer()

    class Meta:
        model = TabletImage
        fields = "__all__"


class GlyphSerializer(serializers.HyperlinkedModelSerializer):
    tablet = TabletSerializer()

    class Meta:
        model = Glyph
        fields = "__all__"
