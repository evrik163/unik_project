from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.homere, name="machine"),
    path('list/', views.show, name='list')
    ]

