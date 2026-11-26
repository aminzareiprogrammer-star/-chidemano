from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=200, verbose_name="نام محصول")),
                ("description", models.TextField(blank=True, verbose_name="توضیحات")),
                ("price", models.DecimalField(decimal_places=0, max_digits=14, verbose_name="قیمت (تومان)")),
                ("category", models.CharField(max_length=100, verbose_name="دسته‌بندی")),
                ("image_url", models.URLField(blank=True, verbose_name="آدرس تصویر")),
                ("is_available", models.BooleanField(default=True, verbose_name="موجود است؟")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")),
            ],
            options={"db_table": "product", "ordering": ["-created_at"], "verbose_name": "محصول", "verbose_name_plural": "محصولات"},
        ),
    ]
