from rest_framework import serializers
from trainbuddy_be.models import Location


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields= ('timestamp','lat','lon')
