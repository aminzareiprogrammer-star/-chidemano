from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True
    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]
    operations = [
        migrations.CreateModel(
            name="ContactMessage",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=120, verbose_name="نام و نام خانوادگی")),
                ("email", models.EmailField(max_length=254, verbose_name="ایمیل")),
                ("subject", models.CharField(max_length=180, verbose_name="موضوع")),
                ("message", models.TextField(verbose_name="متن پیام")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ارسال")),
                ("is_read", models.BooleanField(default=False, verbose_name="بررسی شده؟")),
                ("user", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="contact_messages", to=settings.AUTH_USER_MODEL, verbose_name="کاربر ثبت‌کننده")),
            ],
            options={"verbose_name": "پیام تماس", "verbose_name_plural": "پیام‌های تماس", "ordering": ["-created_at"]},
        ),
    ]
