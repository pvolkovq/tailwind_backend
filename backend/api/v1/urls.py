from rest_framework.routers import DefaultRouter
from .views import PortfolioModelViewSet, ArtworkModelViewSet

router = DefaultRouter()

router.register(r'portfolios', PortfolioModelViewSet, basename='portfolio')
router.register(r'artworks', ArtworkModelViewSet, basename='artwork')

urlpatterns = router.urls