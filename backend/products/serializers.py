from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product

# to validate the title field (another method to validate)
from . import validators

# serializer from api app
from api.serializers import UserPublicSerializer


# serializer to see every product of the user (copied from api.serializers.py)
"""class ProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(view_name="product-detail", lookup_field='pk', read_only=True)
    title = serializers.CharField(read_only=True)"""





class ProductSerializer(serializers.ModelSerializer):
    #  if we want to name the field 'my_discount' instead of 'get_discount'
     my_discount = serializers.SerializerMethodField(read_only=True)
      
     # (first method) url to see the details of a product
     # url = serializers.SerializerMethodField(read_only=True)

     # url to see the details of a product (another method) (clickable url)
     # url = serializers.HyperlinkedIdentityField(view_name="product-detail", lookup_field='pk')

     # write_only will show the field only where you want to create a product. (not on the details of a product)
     # email = serializers.EmailField(write_only=True)
     
     # url to update the product
     # edit_url = serializers.SerializerMethodField(read_only=True)
     
     # create a method 'validate_title' in validators.py and use it like this to validate the field of your choice.
     title = serializers.CharField(validators=[validators.unique_product_title, validators.validate_title_no_hello])

     # if you want something in the data to be same, source='' will help in that.
     # name = serializers.CharField(source='title', read_only=True)

     #  to show the user's data like his username 
     # my_user_data = serializers.SerializerMethodField(read_only=True)

     # to show the user's data like his username (another way by using serializers)
     owner = UserPublicSerializer(source="user", read_only=True)

     # field of this serializer that is connected to the another serializer and showing all the products of the user.
     # related_products = ProductInlineSerializer(source='user.product_set.all', read_only=True, many=True)
     
     # in order to update the content field, this must be done so that when we're to update, it should have body field also.
     body = serializers.CharField(source='content')
     class Meta:
          model = Product
          fields = [
               'owner',
               'id',
               'title', 
               'body',
               'price',
               'sales_price',
               'my_discount',
               'public',
               'endpoint',
               # 'url',
               # 'edit_url',
               # 'email',
               # 'name',
               # 'my_user_data',
               # 'related_products',
          ]
     
     # to show the user's data like his username (one way by using method)
     """def get_my_user_data(self, obj):
          return{
               "username": obj.user.username
          }"""



     # validation with serializers: (one way to do it) field level validation:
     # def validate_title(self, value):
     #      # ignoring the case-insensitive words
     #      qs = Product.objects.filter(title__iexact=value)
     #      if qs.exists():
     #           raise serializers.ValidationError(f"{value} is already a product name!")
     #      return value



     """def create(self, validated_data):
          # unpacking the validated_data
          # return Product.objects.create(**validated_data)
          # to exclude the email field from the validated data by using the pop method of the dictionary.
          # email = validated_data.pop('email')
          obj = super().create(validated_data)
          # print(email, obj.title)
          return obj"""
     

     """def update(self, instance, validated_data):
          email = validated_data.pop('email')
          return super().update(instance, validated_data)"""
     

     # url to see the details of a product (first method)
     """ def get_url(self, obj):
          # return f"api/products/{obj.pk}"

          # sometimes the context is none sometimes not.
          request = self.context.get('request')
          if request is None:
               return None
          return reverse("product-detail", kwargs={'pk': obj.pk}, request=request) """
     

     # url to edit the detail of a product
     """def get_edit_url(self, obj):
          # return f"api/products/{obj.pk}"

          # sometimes the context is none sometimes not.
          request = self.context.get('request')
          if request is None:
               return None
          return reverse("product-edit", kwargs={'pk': obj.pk}, request=request)"""
     


    #  obj is the instance that's being called from the random query
     def get_my_discount(self, obj):
          if not hasattr(obj, 'id'):
               return None
          if not isinstance(obj, Product):
               return None
          return obj.get_discount()
     