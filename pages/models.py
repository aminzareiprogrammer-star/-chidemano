from django.conf import settings
from django.db import models


class ContactMessage(models.Model):
    """پیام‌های ارسال‌شده از فرم تماس با ما."""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="contact_messages", verbose_name="کاربر ثبت‌کننده")
    name = models.CharField("نام و نام خانوادگی", max_length=120)
    email = models.EmailField("ایمیل")
    subject = models.CharField("موضوع", max_length=180)
    message = models.TextField("متن پیام")
    created_at = models.DateTimeField("تاریخ ارسال", auto_now_add=True)
    is_read = models.BooleanField("بررسی شده؟", default=False)

    class Meta:
        db_table = "contact"
        ordering = ["-created_at"]
        verbose_name = "پیام تماس"
        verbose_name_plural = "پیام‌های تماس"

    def __str__(self):
        return f"{self.name} - {self.subject}"
