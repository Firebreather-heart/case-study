from django.urls import path 
from . import views 

urlpatterns = [ 
    path('', views.index, name='home'),
    path('latest/', views.latest, name='latest'),
    path('search/', views.search, name='search'),
]