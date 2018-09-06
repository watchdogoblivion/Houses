from django.contrib import admin
from django.urls import include,path
from .import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('search/', views.IndexSearchView.as_view(), name='search'),
    path('<pk>/', views.LocationView.as_view(), name="property"),
    path('<int:id>/<pk>/', views.PropertyDetail.as_view(), name="propertyview"),
    
]