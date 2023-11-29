from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from products.models import Product
from products.serializers import ProductSerializer



# Create your views here.
# search based on algolia_search engine:
from . import client
class SearchListView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        user = None
        if request.user.is_authenticated:
            user = request.user.username
        query = request.GET.get('q')
        public = str(request.GET.get('public')) != "0"
        tag = request.GET.get('tag') or None
        # print(user, query, public, tag)
        if not query:  
            return Response('', status=400)
        results = client.perform_search(query, tags=tag, user=user, public=public)
        return Response(results)
 


# to show list of the products based on the search:( old approach / not in use )
class SearchListOldView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs) 

        # query that'll show the product title or content
        q = self.request.GET.get('q')
        
        # if q is none
        results = Product.objects.none()
        
        if q is not None:
           user = None
           if self.request.user.is_authenticated:
               user = self.request.user
           results = qs.search(q, user=user)
        return results
    



