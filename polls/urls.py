from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mars/', views.mars, name='mars'),
]