# frontend/urls.py

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.form_view, name='form_view'),
    path('submit/', views.submit_data, name='submit_data'),
]

# Add the static files serving configuration
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

