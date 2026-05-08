from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets, filters
from rest_framework.permissions import AllowAny, IsAuthenticated
from api.v1.permissions import IsPortfolioOwner
from tailwind.models import Portfolio, Artwork
from api.v1.serializers import PortfolioSerializer, ArtworkSerializer, PublicPortfolioArtworkSerializer

class PortfolioModelViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, IsPortfolioOwner)
    serializer_class = PortfolioSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ['is_commissioning_open']
    search_fields = ['user__username']

    queryset = Portfolio.objects.all()

class PortfolioPublicApiView(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = (AllowAny,)
    serializer_class = PortfolioSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ['is_commissioning_open']
    search_fields = ['user__username']

    queryset = Portfolio.objects.filter(is_public=True)


class PublicPortfolioArtwork(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = (AllowAny,)
    serializer_class = PublicPortfolioArtworkSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ['is_commissioning_open']
    search_fields = ['user__username']
    
    queryset = Portfolio.objects.filter(is_public=True)


class ArtworkModelViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ArtworkSerializer
    
    queryset = Artwork.objects.all()