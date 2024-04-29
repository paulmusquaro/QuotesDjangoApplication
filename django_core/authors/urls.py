from django.urls import path
from . import views

app_name = 'authors'

urlpatterns = [
    path('detail/<int:pk>', views.detail, name='detail'),
    path('insert/', views.insert, name='insert'),

]