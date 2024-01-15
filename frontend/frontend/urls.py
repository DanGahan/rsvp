# frontend/urls.py

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.form_view, name='form_view'),
    path('submit/', views.submit_data, name='submit_data'),
    path('success/', views.success_page_view, name='success_page'),
    path('all_rsvps/', views.get_all_rsvps, name='get_all_rsvps'),
   path('header/', views.header_view, name='header_view'), 
]

# Add the static files serving configuration
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

