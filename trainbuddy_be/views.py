from rest_framework import viewsets
from trainbuddy_be.models import Location
from trainbuddy_be.serializers import LocationSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
