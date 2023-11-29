from algoliasearch_django import algolia_engine


# returns the Algolia client object that is used to communicate with the Algolia API.
def get_client():
    return algolia_engine.client


#  returns the Algolia index object that corresponds to the given index name.
def get_index(index_name="cfe_Product"):
    client = get_client()
    # returns an instance of the SearchIndex class, which represents an Algolia index.
    index = client.init_index(index_name)
    return index


def perform_search(query, **kwargs):
    index = get_index()
    params = {}
    tags = ""
    if "tags" in kwargs:
        # tags are arbitary strings that can be assigned to the objects and used as filters
        tags = kwargs.pop("tags") or []
        if len(tags) != 0:
            params['tagFilters'] = tags
    index_filters = [f"{k}:{v}" for k,v in kwargs.items() if v]
    if len(index_filters) != 0:
        params['facetFilters'] = index_filters
    results = index.search(query, params)
    return results

