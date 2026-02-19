from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from restaurant.models import Menu

# To test views/endpoints in Django/DRF, you typically:
#   Create test data in setUp()
# Use Django’s Client or DRF’s APIClient to call the endpoint
#   Assert status codes + response payload
# Since you’re testing DRF views, use DRF’s APIClient.

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Create a normal user and authenticate
        self.user = User.objects.create_user(username="tester", password="pass1234!")
        self.client.force_authenticate(user=self.user)

        # Create test data
        Menu.objects.create(title="IceCream", price="8.00", inventory=50)
        Menu.objects.create(title="Burger", price="10.00", inventory=20)

    def test_getall(self):
        # Adjust path if yours is different (e.g., "/api/menu/")
        response = self.client.get("/api/menu/")

        # compares response status code with expected code 200 OK
        self.assertEqual(response.status_code, 200)

        # If pagination is ON, data is in response.data["results"]
        data = response.data.get("results", response.data)

        # self.assertEqual(len(data), 2) verifies that the API returned two menu 
        # items, matching the two objects created in the test setup().
        # - View is connected
        # - Database objects exist
        # - Queryset is correct
        # - Serialization worked
        self.assertEqual(len(data), 2)

        # Because you order_by("title"), Burger comes before IceCream
        self.assertEqual(data[0]["title"], "Burger")
        self.assertEqual(data[1]["title"], "IceCream")


# IMPORTANT: If you’re using TokenAuthentication instead of Session, 
# Use force_authenticate (Example) fastest for unit tests):

# Testing POST (create)

# If you implemented “admin can write, users can read”, test both:

class MenuCreateTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="u1", password="pass1234!")
        self.admin = User.objects.create_user(username="admin1", password="pass1234!", is_staff=True)

    def test_non_admin_cannot_create(self):
        self.client.force_authenticate(user=self.user)
        payload = {"title": "Pizza", "price": "12.00", "inventory": 10}
        r = self.client.post("/api/menu/", payload, format="json")
        self.assertEqual(r.status_code, status.HTTP_403_FORBIDDEN)

    def test_admin_can_create(self):
        self.client.force_authenticate(user=self.admin)
        payload = {"title": "Pizza", "price": "12.00", "inventory": 10}
        r = self.client.post("/api/menu/", payload, format="json")
        self.assertEqual(r.status_code, status.HTTP_201_CREATED)
        self.assertEqual(r.data["title"], "Pizza")
