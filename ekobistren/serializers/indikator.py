from rest_framework import serializers
from ekobistren.models import indikator


class indikatorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = indikator
        fields = ['indikator', 'keterangan']
