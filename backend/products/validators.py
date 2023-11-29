from rest_framework import serializers
from .models import Product
from rest_framework.validators import UniqueValidator


"""def validate_title(self, value):
    # ignoring the case-insensitive words
    qs = Product.objects.filter(title__iexact=value)
    if qs.exists():
        raise serializers.ValidationError(f"{value} is already a product name!")
    return value
"""

def  validate_title_no_hello(value):
    if "hello" in value.lower():
        raise serializers.ValidationError(f"{value} not allowed!")

unique_product_title = UniqueValidator(queryset=Product.objects.all(), lookup='iexact')