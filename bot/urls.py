from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index_view" ),
    #path('register/', views.register, name='register_view' ),
    
]
