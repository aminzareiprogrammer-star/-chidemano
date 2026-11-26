from django.db import models


class Product(models.Model):
    """محصول قابل مدیریت از پنل ادمین چیدمانو."""
    name = models.CharField("نام محصول", max_length=200)
    description = models.TextField("توضیحات", blank=True)
    price = models.DecimalField("قیمت (تومان)", max_digits=14, decimal_places=0)
    category = models.CharField("دسته‌بندی", max_length=100)
    image_url = models.URLField("آدرس تصویر", blank=True)
    is_available = models.BooleanField("موجود است؟", default=True)
    created_at = models.DateTimeField("تاریخ ایجاد", auto_now_add=True)

    class Meta:
        db_table = "product"
        ordering = ["-created_at"]
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"

    def __str__(self):
        return self.name
