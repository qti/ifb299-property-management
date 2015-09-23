from haystack import indexes
from .models import Property

class PropertyIndex(indexes.SearchIndex, indexes.Indexable):
    """
    Provides fields to Haystack search functionality for indexing
    """
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    rent_cost = indexes.CharField(model_attr='rent_cost')
    address = indexes.CharField(model_attr='address')
    pets_allowed = indexes.BooleanField(model_attr='pets_allowed')
    contact_information = indexes.CharField(model_attr='contact_information')
    property_type = indexes.CharField(model_attr='property_type')

    def get_model(self):
        return Property

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter()
