from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('signout/', views.signout, name='signout'),
    path('faqs/', views.faqs, name='faqs'),
    path('public/', views.public, name='public'),
    path('publicadd/', views.publicaddPhoto, name='publicadd'),
]