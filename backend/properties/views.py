from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Property
from .serializers import PropertySerializer

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all().order_by('-created_at')
    serializer_class = PropertySerializer

    # 👇 Agregamos filtros, búsquedas y ordenamiento
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['property_type', 'city', 'province']
    search_fields = ['title', 'description', 'address', 'city']
    ordering_fields = ['price', 'created_at']
