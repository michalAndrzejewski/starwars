from django.urls import path
from . import views


urlpatterns = [
    path('people', views.people, name='people'),
    path('collections', views.collections, name='collections'),
    path('download', views.download_data, name='download_data'),
]