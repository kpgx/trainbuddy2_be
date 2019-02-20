from rest_framework import serializers
from trainbuddy_be.models import Location


# class LocationSerializer(serializers.Serializer):
    # timestamp = serializers.IntegerField()
    # lat = serializers.FloatField()
    # lon = serializers.FloatField()
    #
    # def create(self, validated_data):
    #     return Location.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.timestamp = validated_data.get('timestamp', instance.timestamp)
    #     instance.lat = validated_data.get('lat', instance.lat)
    #     instance.lon = validated_data.get('lon', instance.lon)
    #     instance.save()
    #     return instance

class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields= ('timestamp','lat','lon')
