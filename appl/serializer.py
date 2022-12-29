from rest_framework import serializers, viewsets
from appl.models import dht
class Dhser(serializers.ModelSerializer):
    class Meta:
        model = dht
        fields = ['id', 'temp','dt']