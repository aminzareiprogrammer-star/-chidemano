from django.contrib.admin.sites import site
from django.test import TestCase
from .admin import ProductAdmin
from .models import Product


class ProductAdminTests(TestCase):
    def test_product_is_registered_in_admin(self):
        self.assertIn(Product, site._registry)

    def test_product_can_be_saved(self):
        product = Product.objects.create(name="صندلی چوبی", price=2500000, category="مبلمان")
        self.assertEqual(Product.objects.get(pk=product.pk).name, "صندلی چوبی")
