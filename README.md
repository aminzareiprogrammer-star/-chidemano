# چیدمانو

## قابلیت‌های تکلیف ذخیره‌سازی در پایگاه داده

- فرم «تماس با ما» با `ContactForm` اعتبارسنجی می‌شود و پیام‌ها در جدول `contact` ذخیره می‌شوند. پیام کاربر واردشده به حساب او متصل می‌شود و پیام مهمان نیز قابل ثبت است.
- فرم ثبت‌نام با `UserCreationForm` کاربر عادی را در جدول استاندارد `auth_user` ذخیره می‌کند. گذرواژه با سازوکار امن Django هش می‌شود؛ کاربر جدید دسترسی مدیریتی ندارد.
- مدل `Product` در اپ `products` تعریف شده و در پنل مدیریت Django ثبت شده است. مدیر می‌تواند محصول جدید درج، ویرایش، جست‌وجو و فیلتر کند. جدول آن `product` است.

## اجرا

```bash
python -m pip install "Django>=5.2,<6.2"
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

پنل مدیریت: `http://127.0.0.1:8000/admin/`

## آزمون‌ها

```bash
python manage.py test
```

## نسخه تکلیف

Git tag: `assignment-db-crud-v1`
