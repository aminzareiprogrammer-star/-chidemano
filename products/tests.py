from django.test import TestCase
from django.urls import reverse

from .models import Product


class ProductPagesTests(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name="صندلی چوبی",
            description="صندلی با طراحی ساده",
            price=2500000,
            category="مبلمان",
            image_url="",
            is_available=True,
        )

    def test_catalog_displays_products_from_database(self):
        response = self.client.get(reverse("products:catalog"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "صندلی چوبی")
        self.assertContains(response, reverse("products:detail", args=[self.product.pk]))

    def test_detail_displays_product_selected_by_id(self):
        response = self.client.get(reverse("products:detail", args=[self.product.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["product"], self.product)
        self.assertContains(response, "صندلی با طراحی ساده")

    def test_unknown_product_returns_404(self):
        response = self.client.get(reverse("products:detail", args=[999999]))
        self.assertEqual(response.status_code, 404)
