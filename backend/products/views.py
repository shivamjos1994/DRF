from rest_framework import generics, mixins, permissions, authentication
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

from .models import Product
from .serializers import ProductSerializer
from api.mixins import (StaffEditorPermissionMixin, UserQuerySetMixin)
# from api.permissions import IsStaffEditorPermission
# from api.authentication import TokenAuthentication


# for listing a queryset or creating a model instance.
class ProductListCreateAPIView(UserQuerySetMixin, StaffEditorPermissionMixin, generics.ListCreateAPIView):
    queryset = Product.objects.all()
    # assigns the ProductSerializer class as the serializer for this view.
    serializer_class = ProductSerializer

    # can change the user_field in here:
    # user_field = " " (field must be field from serializer)
    

    # write the authentication_by_default in settings.py
    # authentication_classes = [authentication.SessionAuthentication, TokenAuthentication]

    # permission to view and create the data
    # permission_classes = [permissions.IsAuthenticated]

    # permission to view the data but requires permission to create one.
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # It ensures that the user is authenticated, and has the appropriate `add`/`change`/`delete` permissions on the model.
    # permission_classes = [permissions.DjangoModelPermissions]

    # custom permission(first check the permission by the admin, then will check the other IsStaffEditorPermission)
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]


    def perform_create(self, serializer):
        # email = serializer.validated_data.pop('email')
        # print(email)
        
        #  The serializer.validated_data dictionary contains the validated data from the request.
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        # This method saves the validated data to the database and returns the created object. 
        # The keyword argument overrides the value of the content attribute in the validated data.
        serializer.save(user=self.request.user, content=content)


    # another method to do this by mixins and importing it here (only the user can see his added data)
    """def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        request = self.request
        user = request.user
        if not user.is_authenticated:
            return Product.objects.none()
        # print(request.user)
        return qs.filter(user=request.user)"""

product_list_create_view = ProductListCreateAPIView.as_view()



# for retrieving a model instance
class ProductDetailAPIView(UserQuerySetMixin, StaffEditorPermissionMixin, generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # now we don't need the permission here, we've imported a customized mixin from api.mixins
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

# This allows us to discover information about the view when we do URL reverse lookups. 
product_detail_view = ProductDetailAPIView.as_view()


# #  for listing a queryset. 
# class ProductListAPIView(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# product_list_view = ProductListAPIView.as_view()



# for updating a model instance.
class ProductUpdateAPIView(UserQuerySetMixin, StaffEditorPermissionMixin, generics.UpdateAPIView):
    queryset = Product.objects.all()
    # This attribute is used to validate and serialize the object data before and after updating it.
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission] 
  
    def perform_update(self, serializer):
        # This method saves the validated data to the database and returns the updated object.
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title

product_update_view = ProductUpdateAPIView.as_view()



# for deleting a model instance.
class ProductDestroyAPIView(UserQuerySetMixin, StaffEditorPermissionMixin, generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]
   
    def perform_destroy(self, instance):
        super().perform_destroy(instance)

product_destroy_view = ProductDestroyAPIView.as_view()



# mixins( use class based functions instead of condition like [if method=='POST'])
class ProductMixinView(
    mixins.CreateModelMixin, 
    mixins.ListModelMixin, 
    mixins.RetrieveModelMixin, 
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    # get method
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    # post method
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = "This is created to check CreateModelMixin"
        serializer.save(content=content)

    
    # put method
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title


    # delete method
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    def perform_destroy(self, instance):
        super().perform_destroy(instance)
    
    

product_mixin_view = ProductMixinView.as_view()














# Or can use function based view:
"""@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method

    if method == "GET":
        if pk is not None:
            # detail view
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)
        # list view
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)


    if method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"invalid": "Not good data"}, status=400)"""
    

