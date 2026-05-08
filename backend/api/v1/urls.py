from rest_framework.routers import DefaultRouter
from .views import PortfolioModelViewSet, ArtworkModelViewSet, PortfolioPublicApiView, PublicPortfolioArtwork

router = DefaultRouter()

router.register(r'portfolios', PortfolioModelViewSet, basename='portfolio')
router.register(r'public-portfolios', PortfolioPublicApiView, basename='public-portfolio')
router.register(r'public-portfolios-artworks', PublicPortfolioArtwork, basename='public-portfolio-artwork')
router.register(r'artworks', ArtworkModelViewSet, basename='artwork')

urlpatterns = router.urls