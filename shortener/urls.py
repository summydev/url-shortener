from django.urls import path, include
from . import views
from .views import ShortURLListCreateAPIView, ShortURLDetailAPIView, redirect_to_original, direct_redirect

urlpatterns = [
    # API endpoints
    path('api/shorturls/', ShortURLListCreateAPIView.as_view(), name='api-shorturl-list'),
    path('api/shorturls/<str:short_code>/', ShortURLDetailAPIView.as_view(), name='api-shorturl-detail'),
    path('api/redirect/<str:short_code>/', redirect_to_original, name='api-redirect'),
    path('api/docs/', views.api_docs, name='api-docs'),
    # Direct browser redirect (keep for backward compatibility)
    path('<str:short_code>/', direct_redirect, name='redirect'),
]