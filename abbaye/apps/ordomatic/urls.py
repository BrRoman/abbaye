""" apps/ordomatic/urls.py """

from django.urls import path

from . import views

app_name = 'ordomatic'
urlpatterns = [
    path('', views.home, name='home'),
    path('pdf/<int:year>/', views.pdf, name='pdf'),
]
