from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.homere, name="machine"),
    path('list/', views.show, name='list'),
    path('retrain/', views.retrain, name='re'),
    path('post/<int:post_id>/', views.show_post, name='post')
    ]

