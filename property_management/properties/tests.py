"""
Contains unit tests for the properties app
"""
from django.test import TestCase
from django.core.urlresolvers import reverse

# Selenium imports
from django.test import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

import unittest, time, re

from .models import Property

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

class PropertyViewsTests(TestCase):
    def setUp(self):
        """
        Instantiate test properties
        """
        self.test_property_one = Property.objects.create(
            address = "27 Foo, dev null place, 1337",
            pets_allowed = False,
            bedrooms = 50,
            property_type = "house",
            bathrooms = 3,
            car_spaces = 2,
            contact_information = " { 'test': field, 'another': field } ",
        )

        self.test_property_two = Property.objects.create(
            name = "Foo Place",
            address = "99 Foo, dev null place, 0000",
            description = "Foo foo, foo; foo, foo; foo!",
            contact_information = " { 'test': field, 'another': field } ",
            image="http://i.imgur.com/81qyN1y.jpg",
        )

        self.test_property_three = Property.objects.create(
            address = "42 Foo, dev null place, 9999",
            description = "Foo foo, foo; foo, foo; foo!",
            pets_allowed = True,
        )

        self.test_property_four = Property.objects.create(
            address = "356 Foo, dev null place, 12345",
            description = "Foo foo, foo; foo, foo; foo!",
            pets_allowed = False,
            contact_information = " { 'test': field, 'another': field } ",
        )

    def test_properties_pk(self):
        resp = self.client.get(reverse('properties:list'))

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(
                [properties.pk for properties in
                    resp.context['properties']],[1, 2, 3, 4]
            )

    def test_properties_view(self):
        resp = self.client.get(reverse('properties:list'))

        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.test_property_one, resp.context['properties'])
        self.assertIn(self.test_property_three, resp.context['properties'])

        self.assertContains(resp, self.test_property_three.name)
        self.assertContains(resp, self.test_property_one.name)

        self.assertTemplateUsed(resp, 'properties/properties.html')

    def test_properties_pets_allowed(self):
        resp = self.client.get(reverse('properties:list'))

        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.test_property_two,
            resp.context['properties'].filter(pets_allowed=False))
        self.assertIn(self.test_property_three,
            resp.context['properties'].filter(pets_allowed=True))

    def test_properties_images(self):
        resp = self.client.get(reverse('properties:list'))

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(
                resp.context['properties'].get(pk=2).image,
                self.test_property_two.image
            )

    def test_property_view(self):
        resp = self.client.get(reverse('properties:detail', kwargs={
                'pk': self.test_property_two.pk
            }))

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(
                self.test_property_two,
                resp.context['individual_property']
            )

        self.assertContains(resp, self.test_property_two.name)
        self.assertTemplateUsed(resp, 'properties/property.html')

    def test_property_description(self):
        resp = self.client.get(reverse('properties:detail', kwargs={
                'pk': self.test_property_four.pk
            }))

        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, self.test_property_four.description)

    def test_property_image(self):
        resp = self.client.get(reverse('properties:detail', kwargs={
                'pk': self.test_property_two.pk
            }))

        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, self.test_property_two.image)

    def test_bedrooms(self):
        resp = self.client.get(reverse('properties:list'))

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(
                resp.context['properties'].get(pk=1).bedrooms,
                self.test_property_one.bedrooms
            )

    def test_property_type(self):
        resp = self.client.get(reverse('properties:list'))

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(
                resp.context['properties'].get(pk=1).property_type,
                self.test_property_one.property_type
            )    

    def test_bathrooms(self):
        resp = self.client.get(reverse('properties:list'))

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(
                resp.context['properties'].get(pk=1).bathrooms,
                self.test_property_one.bathrooms
            ) 

    def test_car_spaces(self):
        resp = self.client.get(reverse('properties:list'))

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(
                resp.context['properties'].get(pk=1).car_spaces,
                self.test_property_one.car_spaces
            )           


class SeleniumTests(LiveServerTestCase):
    """
    Selenium tests, good for acceptance testing; prefer Django's inbuilt unit
    testing functionality over selenium for models & views
    """
    def setUp(self):
        """
        Instantiate test properties
        """
        self.test_property_one = Property.objects.create(
            address = "27 Foo, dev null place, 1337",
            pets_allowed = False,
            rent_cost = 400,
            contact_information = " { 'test': field, 'another': field } ",
        )

        self.test_property_two = Property.objects.create(
            name = "Foo Place",
            address = "99 Foo, dev null place, 0000",
            rent_cost = 200,
            description = "Foo foo, foo; foo, foo; foo!",
            contact_information = " { 'test': field, 'another': field } ",
            image="http://i.imgur.com/81qyN1y.jpg",
        )

        self.test_property_three = Property.objects.create(
            address = "42 Foo, dev null place, 9999",
            rent_cost = 300,
            description = "Foo foo, foo; foo, foo; foo!",
            pets_allowed = True,
        )

        self.test_property_four = Property.objects.create(
            address = "356 Foo, dev null place, 12345",
            description = "Foo foo, foo; foo, foo; foo!",
            pets_allowed = False,
            contact_information = " { 'test': field, 'another': field } ",
        )

    @classmethod
    def setUpClass(cls):
        super(SeleniumTests, cls).setUpClass()
        cls.selenium = WebDriver()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(SeleniumTests, cls).tearDownClass()

    def test_index(self):
        self.selenium.get(self.live_server_url)
        self.selenium.find_element_by_link_text("Home")
        self.selenium.find_element_by_link_text("Properties")
        self.selenium.find_element_by_link_text("About")
        self.selenium.find_element_by_link_text("Login")
        self.selenium.find_element_by_link_text("View Properties")

    def test_property_list(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/properties/'))
        self.selenium.find_element_by_link_text("Home")
        self.selenium.find_element_by_link_text("Properties")
        self.selenium.find_element_by_link_text("About")
        self.selenium.find_element_by_link_text("Login")

    def test_search_bar(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/properties/'))
        self.selenium.find_element_by_name("q").clear()      
        self.selenium.find_element_by_name("q").send_keys("200")
        time.sleep(1)
        self.selenium.find_element_by_xpath("//button[@type='submit']").click()

    def test_filter_lowhigh(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/properties/'))
        self.selenium.find_element_by_xpath("(//button[@type='button'])[11]").click()
        Select(self.selenium.find_element_by_id("SortSelect")).select_by_visible_text("Price: Lowest to highest")
        self.selenium.find_element_by_css_selector("option[value=\"myorder:asc\"]").click()
        self.selenium.find_element_by_css_selector("button.close").click()

    def test_filter_highlow(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/properties/'))
        self.selenium.find_element_by_xpath("(//button[@type='button'])[11]").click()
        Select(self.selenium.find_element_by_id("SortSelect")).select_by_visible_text("Price: Highest to lowest")
        self.selenium.find_element_by_css_selector("option[value=\"myorder:asc\"]").click()
        self.selenium.find_element_by_css_selector("button.close").click()
