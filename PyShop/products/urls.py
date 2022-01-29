from django.urls import path
from . import views


urlpatterns = [
    path('', views.index)  # passing the reference to the index
]