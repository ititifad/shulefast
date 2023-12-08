# filters.py
import django_filters
from core.models import School, Region, SubCategory

class SchoolFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', label='School Name')
    region = django_filters.ModelChoiceFilter(queryset=Region.objects.all(), label='Region')
    
    location = django_filters.CharFilter(lookup_expr='icontains', label='Location')

    class Meta:
        model = School
        fields = ['name', 'region', 'location']
