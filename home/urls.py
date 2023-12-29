from django.urls import path
from . import views

urlpatterns=[
    path('',views.homepage,name='home'),
    path('pricing',views.pricing,name='pricing')
]