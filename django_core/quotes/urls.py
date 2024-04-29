from django.urls import path, include
from . import views

app_name = "quotes"

urlpatterns = [
    path("", views.main, name="main"),
    path("<int:page>", views.main, name="root_paginate"),
    path("insert/", views.insert, name="insert"),
    path("find/<tag_name>", views.find, name="find"),
]
