# import json
# Return a dict containing the data in instance
# from django.forms import model_to_dict
# from django.http import JsonResponse
from products.models import Product

from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer


# Create your views here.

@api_view(["GET"])
def api_homeGet(request, *args, **kwargs):
    # generate a random data from db
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        # can select fields accordingly
        # data = model_to_dict(instance, fields=['id', 'title', 'content', 'price', 'sales_price'])
        
        # by using serializer, there is no need to convert 'model_to_dict' by ourselves.
        data = ProductSerializer(instance).data
    # return JsonResponse(data)
    return Response(data)
    
    


@api_view(["POST"])
def api_homePost(request, *args, **kwargs):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # serializer.save()
        print(serializer.data)
        return Response(serializer.data)
    return Response({"invalid": "not good data"}, status=400)