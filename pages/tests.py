from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from .models import ContactMessage


class ContactAndRegistrationTests(TestCase):
    def test_contact_form_saves_message(self):
        response = self.client.post(reverse("pages:contact"), {
            "name": "کاربر آزمایشی", "email": "test@example.com",
            "subject": "سؤال", "message": "متن پیام آزمایشی",
        })
        self.assertRedirects(response, reverse("pages:contact"))
        self.assertEqual(ContactMessage.objects.count(), 1)
        self.assertEqual(ContactMessage.objects.first().subject, "سؤال")

    def test_registration_creates_normal_user(self):
        response = self.client.post(reverse("pages:register"), {
            "first_name": "علی", "last_name": "رضایی", "username": "ali",
            "email": "ali@example.com", "password1": "StrongPass!8392",
            "password2": "StrongPass!8392",
        })
        self.assertRedirects(response, reverse("pages:home"))
        user = User.objects.get(username="ali")
        self.assertTrue(user.check_password("StrongPass!8392"))
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
