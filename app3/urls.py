from django.urls import path 
from app3.views import *
app_name='nothing'
urlpatterns=[
    path('three/', three, name='three'), 
]