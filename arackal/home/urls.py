from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="home"),
    path('plumbing/', views.plumbing, name="plumbing"),
    path('heating/', views.heating, name="heating"),
    path('appliances/', views.appliances, name="appliances"),


    path('background/', views.faucet_background, name="background"),
    #path('test/', views.test, name="test"),

]