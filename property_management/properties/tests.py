"""
Contains unit tests for the properties app
"""
from django.test import TestCase

from .models import Property

# def setUp(self):
#     self.test_property_one = Property.objects.create(
#         address = "27 Foo, dev null place, 1337",
#         pets_allowed = False,
#         contact_information = " { 'test': field, 'another': field } ",
#     )

#     self.test_property_two = Property.objects.create(
#         address = "99 Foo, dev null place, 0000",
#         description = "Foo foo, foo; foo, foo; foo!",
#         contact_information = " { 'test': field, 'another': field } ",
#     )

#     self.test_property_three = Property.objects.create(
#         address = "42 Foo, dev null place, 9999",
#         description = "Foo foo, foo; foo, foo; foo!",
#         pets_allowed = False,
#     )

    # self.test_property_four = Property.objects.create(
    #     address = "356 Foo, dev null place, 12345",
    #     description = "Foo foo, foo; foo, foo; foo!",
    #     pets_allowed = False,
    #     contact_information = " { 'test': field, 'another': field } ",
    # )

# Create your tests here.
class PropertyModelTests(TestCase):
    """
    Property model tests
    """
    def test_id_creation(self):
        """
        Tests that creating a property also creates an id
        """
        test_property_one = Property.objects.create(
            address="27 Foo, dev null place, 1337",
            pets_allowed=False,
            contact_information=" { 'test': field, 'another': field } ",
        )

        properties = Property.objects.get(pk=1)
        self.assertEqual(test_property_one, properties)

    def test_id_iteration(self):
        """
        Tests that each new property has a new id created for it
        """
        test_property_one = Property.objects.create(
            address="27 Foo, dev null place, 1337",
            pets_allowed=False,
            contact_information=" { 'test': field, 'another': field } ",
        )

        test_property_two = Property.objects.create(
            address="99 Foo, dev null place, 0000",
            description="Foo foo, foo; foo, foo; foo!",
            contact_information=" { 'test': field, 'another': field } ",
        )

        properties = Property.objects.all().count()
        self.assertEqual(properties, Property.objects.get(pk=2).id)
