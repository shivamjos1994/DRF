from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register

from .models import Product

@register(Product)
class ProductIndex(AlgoliaIndex):
    # to show only the public data to the alogolia. (is_public is a method from products.models.py)
    # should_index = 'is_public'
    fields = [
        'title',
        'body',
        'price',
        'user',
        'public',
        'endpoint',
    ]
    settings = {
        'searchableAttributes': ['title', 'body'],

        # contains the names of the attributes that should be used for faceting. Faceting is a feature that allows creating categories based on specific attributes so that users can filter search results by those categories.
        'attributesForFaceting': ['user', 'public']
    }
    # will be attached to the algolia index and random tags will be assigned to every product (tags are arbitary strings that can be assigned to the objects and used as filters.)
    tags = 'get_tag_list'