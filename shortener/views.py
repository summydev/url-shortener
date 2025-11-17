from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .models import ShortURL
from .forms import URLForm

def home(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            # Create new short URL
            short_url = ShortURL.objects.create(
                original_url=form.cleaned_data['original_url']
            )
            
            # Build the full short URL to display
            base_url = request.build_absolute_uri('/')
            short_url_display = f"{base_url}{short_url.short_code}"
            
            return render(request, 'shortener/home.html', {
                'form': form,
                'short_url': short_url,
                'short_url_display': short_url_display
            })
    else:
        form = URLForm()
    
    return render(request, 'shortener/home.html', {'form': form})

def redirect_view(request, short_code):
    # Find the short URL and redirect to original
    short_url = get_object_or_404(ShortURL, short_code=short_code)
    
    # Update click count
    short_url.click_count += 1
    short_url.save()
    
    return HttpResponseRedirect(short_url.original_url)