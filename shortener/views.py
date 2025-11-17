from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, redirect
from django.http import Http404
from .models import ShortURL
from .serializers import ShortURLSerializer, CreateShortURLSerializer
from django.shortcuts import render

def api_docs(request):
    return render(request, 'shortener/api_docs.html')
class ShortURLListCreateAPIView(generics.ListCreateAPIView):
    queryset = ShortURL.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateShortURLSerializer
        return ShortURLSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Check if custom code is provided and already exists
        custom_code = serializer.validated_data.get('custom_code')
        if custom_code and ShortURL.objects.filter(short_code=custom_code).exists():
            return Response(
                {'error': 'This custom code is already taken.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        instance = serializer.save()
        
        # Return the created object with full details
        response_serializer = ShortURLSerializer(instance, context={'request': request})
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)

class ShortURLDetailAPIView(generics.RetrieveAPIView):
    queryset = ShortURL.objects.all()
    serializer_class = ShortURLSerializer
    lookup_field = 'short_code'

@api_view(['GET'])
def redirect_to_original(request, short_code):
    short_url = get_object_or_404(ShortURL, short_code=short_code)
    
    # Record click statistics
    short_url.click_count += 1
    short_url.save()
    
    return Response({
        'original_url': short_url.original_url,
        'short_code': short_url.short_code,
        'click_count': short_url.click_count
    })

# Keep the actual redirect for direct browser access
def direct_redirect(request, short_code):
    short_url = get_object_or_404(ShortURL, short_code=short_code)
    
    # Update click count
    short_url.click_count += 1
    short_url.save()
    
    return redirect(short_url.original_url)