from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name='home'),

    path('collections/', views.collections, name='collections'),
    path('single_collection/<str:pk>/', views.single_collection, name='single_collection'),

    path('download/', views.download_data, name='download_data'),
]