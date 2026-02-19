# Create your tests here.
from django.test import TestCase
from restaurant.models import Menu

# TestCase class
class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80.00")

# Test Log:

# PS C:\Capstone-project\littlelemon> python manage.py test
# Found 1 test(s).
# Creating test database for alias 'default'...
# System check identified no issues (0 silenced).
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.003s

# OK
# Destroying test database for alias 'default'...

# REMEMBER, item is the object containing price with 2 decimal places
# assertEqual consists of values that you provide and you have to data
# them correctly.  80 will not work because price is not an integer.
# price is a float.  Must use string 80.00