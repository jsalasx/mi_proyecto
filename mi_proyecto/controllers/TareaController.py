from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from ..models import Tarea
from ..serializers.TareaSerializer import TareaSerializer
from ..filters import TareaFilter
from rest_framework.permissions import IsAuthenticated
class TareaListCreate(generics.ListCreateAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TareaFilter
    #filterset_fields = ['fecha_expiracion', 'id','titulo']
    serializer_class = TareaSerializer
    permission_classes = [IsAuthenticated]

class TareaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    permission_classes = [IsAuthenticated]