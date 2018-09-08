from django.contrib import admin
from django.urls import include,path
from .import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('search/', views.IndexSearchView.as_view(), name='search'),
    path('<pk>/', views.PropertiesView.as_view(), name="properties"),
    path('<pk>/searchProperties/', views.PropertiesSearchView.as_view(), name='searchProperties'),
    path('<int:id>/<pk>/', views.PropertyDetail.as_view(), name="propertyview"),
    
]