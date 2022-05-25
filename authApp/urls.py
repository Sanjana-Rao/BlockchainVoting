from django.urls import path
from .import views
from django.contrib.auth import views as auth_view
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',views.home,name="home"),
    path('main/',views.main,name="main"),
    path('registration/',views.Registration, name="registration"),
    path('registration/otp/',views.otpRegistration, name="otp-registration"),
    path('voter-login/',views.voterLogin, name="voter-login"),
    path('admin-login/',views.adminLogin, name="admin-login"),
    path('login/',views.home,name="home"),
    path('login/admin/',views.adminLoggedIn, name="login-admin"),
    path('login/otp/',views.otpLogin, name="otp-login"),
    path('logout/',auth_view.LogoutView.as_view(template_name='home.html')),
    path('email-verify/', views.email_verification, name="email-verify"),
    path('forget-password/',views.forget_password,name="forget-password"),
    path('forget-password/done/',TemplateView.as_view(template_name='forget-password-done.html')),
    path('change-password/<slug:uid>/',views.change_password,name="change-password"),
]

urlpatterns += staticfiles_urlpatterns()