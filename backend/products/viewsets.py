from rest_framework import viewsets, mixins
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """
       get -> List -> queryset
       get -> retrieve -> Product instance detail
       post -> create -> New Instance
       put -> Update
       patch -> Partial Update
       delele -> Destroy

    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'



class ProductGenericViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
       get -> List -> queryset
       get -> retrieve -> Product instance detail
    
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'



