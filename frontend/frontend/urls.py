# frontend/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.form_view, name='form_view'),
    path('api/submit/', views.submit_data, name='submit_data'),
]

