from django import forms

class URLForm(forms.Form):
    original_url = forms.URLField(
        label='Enter your long URL',
        widget=forms.URLInput(attrs={
            'class': 'form-control',
            'placeholder': 'https://example.com/very/long/url...'
        })
    )