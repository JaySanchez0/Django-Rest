from django.urls import include, path
from rest_framework import routers
from . import views

urlpatterns = [
    path('peoples/',views.people_list)
]