from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.permissions import AllowAny
from tailwind.models import Portfolio, Artwork
from api.v1.serializers import PortfolioSerializer, ArtworkSerializer

class PortfolioModelViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = PortfolioSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ['is_commissioning_open']
    search_fields = ['user__username']

    queryset = Portfolio.objects.filter(user__is_superuser=False)

class ArtworkModelViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = ArtworkSerializer
    
    queryset = Artwork.objects.all()