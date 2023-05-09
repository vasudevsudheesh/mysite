from django.urls import path

from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('base/', views.base, name='base'),
    path('contact/', views.contact, name='contact')
]
