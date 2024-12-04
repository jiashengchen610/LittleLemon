from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer
from restaurant.models import MenuItem

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item, "IceCream : 80")

class MenuViewTest(TestCase):
    def setUp(self):
        """Set up the test instances."""
        # Create a few Menu objects for testing purposes
        self.menu_item_1 = MenuItem.objects.create(
            title="Spaghetti Bolognese",
            price=12.99,
            inventory=50
        )
        self.menu_item_2 = MenuItem.objects.create(
            title="Chicken Caesar Salad",
            price=10.99,
            inventory=30
        )
        self.client = APIClient()

def test_getall(self):
    # Send a GET request to the menu endpoint
        response = self.client.get('/restaurant/menu/')

    # Serialize the menu items manually
        menu_items = MenuItem.objects.all()
        serialized_data = MenuItemSerializer(menu_items, many=True).data

    # Check if the response is successful and if the serialized data matches
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serialized_data)