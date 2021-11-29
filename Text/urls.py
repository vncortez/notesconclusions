

from django.urls import path
from Text import views

urlpatterns = [
    path('text/', views.text_viewset, name='api_text'),
    path('types/', views.types_found_viewset, name='api_types'),
]