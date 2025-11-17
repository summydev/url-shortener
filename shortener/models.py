from django.db import models
import string
import random

class ShortURL(models.Model):
    original_url = models.URLField(max_length=2000)
    short_code = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    click_count = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.short_code} -> {self.original_url}"
    
    def save(self, *args, **kwargs):
        # Generate short code if it doesn't exist
        if not self.short_code:
            self.short_code = self.generate_short_code()
        super().save(*args, **kwargs)
    
    def generate_short_code(self):
        characters = string.ascii_letters + string.digits
        short_code = ''.join(random.choices(characters, k=6))
        
        # Make sure it's unique
        while ShortURL.objects.filter(short_code=short_code).exists():
            short_code = ''.join(random.choices(characters, k=6))
        
        return short_code