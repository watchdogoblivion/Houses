from django import forms
from django.contrib.auth.models import User, Group
import django_filters
from .models import Location

class LocationFilter(django_filters.FilterSet):
    location_name = django_filters.CharFilter(lookup_expr='icontains')
    location_type = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Location
        fields = ['location_name', 'location_type']