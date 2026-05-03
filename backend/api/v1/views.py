from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from tailwind.models import Portfolio, Artwork
from api.v1.serializers import PortfolioSerializer, ArtworkSerializer

class PortfolioModelViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = PortfolioSerializer
    
    queryset = Portfolio.objects.all()

class ArtworkModelViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = ArtworkSerializer
    
    queryset = Artwork.objects.all()