from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [


    path('', views.home, name="home" ),
    path('login/', views.loginPage, name="login" ),
    path('register/', views.registerPage, name="register" ),
    path('respo_log1/<str:pk>/', views.rl1Page, name="respo_log1" ),
    path('respo_log2/<str:pk>/', views.rl2Page, name="respo_log2" ),
    path('respo_info/<str:pk>/', views.rinfoPage, name="respo_info" ),
    path('respo_fin/<str:pk>/', views.rfinPage, name="respo_fin" ),
    # path('respo_ca/<str:pk>/', views.rCaPage, name="respo_ca" ),
    path('respo_ca/<str:pk>/', views.RCa, name="respo_ca" ),














]