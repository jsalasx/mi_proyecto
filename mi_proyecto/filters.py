import django_filters
from .models import Tarea

class TareaFilter(django_filters.FilterSet):
    titulo = django_filters.CharFilter(lookup_expr='icontains')
    #descripcion = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Tarea
        fields = ['titulo']  
