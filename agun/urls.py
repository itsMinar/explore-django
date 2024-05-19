from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_agun, name='all_agun'),
]