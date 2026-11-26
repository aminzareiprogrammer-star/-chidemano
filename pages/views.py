from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import RegisterForm, ContactForm


def home(request):
    return render(request, "pages/home.html")


def about(request):
    return render(request, "pages/about.html")


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save(commit=False)
            if request.user.is_authenticated:
                contact_message.user = request.user
            contact_message.save()
            messages.success(request, "پیام شما با موفقیت در سامانه ثبت شد.")
            return redirect("pages:contact")
        messages.error(request, "لطفاً خطاهای فرم را بررسی و دوباره ارسال کنید.")
    else:
        initial = {}
        if request.user.is_authenticated:
            initial = {"name": request.user.get_full_name() or request.user.username, "email": request.user.email}
        form = ContactForm(initial=initial)
    return render(request, "pages/contact.html", {"form": form})


def register(request):
    if request.user.is_authenticated:
        return redirect("pages:home")
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # اطلاعات کاربر در auth_user و رمز عبور به‌صورت هش‌شده ذخیره می‌شود.
            login(request, user)
            messages.success(request, "حساب کاربری شما با موفقیت ساخته شد.")
            return redirect("pages:home")
        messages.error(request, "ثبت‌نام انجام نشد؛ خطاهای فرم را بررسی کنید.")
    else:
        form = RegisterForm()
    return render(request, "pages/register.html", {"form": form})
