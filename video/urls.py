from django.urls import path
from . import views

app_name = 'video'

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload'),
    path('place/<str:destination_value>/', views.place, name='place'),
]
