# automation_app/urls.py
from django.urls import path
from django.contrib import admin
from typing_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.automate_typing, name='automate_typing'),
    path('success/', views.success, name='success'),
]
