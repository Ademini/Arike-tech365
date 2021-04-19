from django.urls import path 
from automobile import views 

urlpatterns = [
    path('', views.home, name='home'),

    path('about', views.about, name='about'),
    
    path('search', views.search, name='search'),
    
    path('cars', views.cars, name='cars'),

    path('<int:id>', views.car_detail,name='car_detail'),
   
    
]