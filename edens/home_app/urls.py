from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('mens/',views.mensWear,name='mens'),
    path('womens/',views.womensWear,name='womens'),
    path('kids/',views.kidsWear,name='kids'),
    path('footwears/',views.footWear,name='footwears'),
]