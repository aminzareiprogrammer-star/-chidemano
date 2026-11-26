from django.shortcuts import get_object_or_404, render

from .models import Product


def catalog(request):
    """نمایش همه محصولات ثبت‌شده در پایگاه داده."""
    products = Product.objects.all()
    return render(request, "products/catalog.html", {"products": products})


def detail(request, pk):
    """نمایش جزئیات یک محصول بر اساس شناسه اصلی آن."""
    product = get_object_or_404(Product, pk=pk)
    return render(request, "products/detail.html", {"product": product})
