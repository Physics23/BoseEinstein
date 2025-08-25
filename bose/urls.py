
# simulator/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.simulator, name='simulator'),  # Home page
    
]