from rest_framework.routers import DefaultRouter
from products.viewsets import ProductViewSet, ProductGenericViewSet


# The default router extends the SimpleRouter, but also adds in a default API root view, and adds format suffix patterns to the URLs.
router = DefaultRouter()

# router.register('products', ProductViewSet, basename='products')
router.register('products', ProductGenericViewSet, basename='products')
# print(router.urls)

urlpatterns = router.urls
