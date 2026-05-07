from rest_framework.routers import DefaultRouter
from .views import PortfolioModelViewSet, ArtworkModelViewSet, PortfolioReadOnlyApiView

router = DefaultRouter()

router.register(r'portfolios', PortfolioModelViewSet, basename='portfolio')
router.register(r'portfolios-view', PortfolioReadOnlyApiView, basename='portfolio-view')
router.register(r'artworks', ArtworkModelViewSet, basename='artwork')

urlpatterns = router.urls