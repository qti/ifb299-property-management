"""
Provides models from which Django will generate the database

Primary key automatically provided by Django for each class
in the form: id = models.AutoField(primary_key=True)
"""

from django.db import models

# Create your models here.
class Property(models.Model):
    """
    Model for an individual property
    """
    name = models.CharField(max_length=255, default='House listing')
    address = models.CharField(max_length=255)
    rent_cost = models.CharField(max_length=50, null='true')
    description = models.TextField()
    pets_allowed = models.BooleanField(default=False)
    contact_information = models.TextField() # refactor into JSON field (maybe)
    # simple link to an imgur file, if no input set to blank field
    image = models.CharField(max_length=128, blank=True, default='')
    image2 = models.CharField(max_length=128, blank=True, default='')
    image3 = models.CharField(max_length=128, blank=True, default='')
    bedrooms = models.CharField(max_length=2, null='true')
    property_type = models.CharField(max_length=50,null='true')
    bathrooms = models.CharField(max_length=2,null='true')
    car_spaces = models.CharField(max_length=2,null='true')

    # Identifies self as address name rather than 'Property Object'
    def __str__(self):
        return self.address
