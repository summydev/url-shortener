from django.urls import path
from .views import ShortURLListCreateAPIView, ShortURLDetailAPIView, redirect_to_original, direct_redirect

urlpatterns = [
    # API endpoints
    path('api/shorturls/', ShortURLListCreateAPIView.as_view(), name='api-shorturl-list'),
    path('api/shorturls/<str:short_code>/', ShortURLDetailAPIView.as_view(), name='api-shorturl-detail'),
    path('api/redirect/<str:short_code>/', redirect_to_original, name='api-redirect'),
    
    # Direct browser redirect (for sharing short links)
    path('<str:short_code>/', direct_redirect, name='redirect'),
]