from rest_framework import serializers
from .models import ShortURL

class ShortURLSerializer(serializers.ModelSerializer):
    short_url = serializers.SerializerMethodField()
    
    class Meta:
        model = ShortURL
        fields = ['id', 'original_url', 'short_code', 'short_url', 'click_count', 'created_at']
        read_only_fields = ['short_code', 'click_count', 'created_at']
    
    def get_short_url(self, obj):
        request = self.context.get('request')
        if request:
            base_url = request.build_absolute_uri('/')
            return f"{base_url}{obj.short_code}"
        return obj.short_code

class CreateShortURLSerializer(serializers.ModelSerializer):
    custom_code = serializers.CharField(
        max_length=15, 
        required=False, 
        allow_blank=True,
        write_only=True
    )
    
    class Meta:
        model = ShortURL
        fields = ['original_url', 'custom_code']
    
    def create(self, validated_data):
        custom_code = validated_data.pop('custom_code', None)
        short_url = ShortURL(**validated_data)
        
        if custom_code:
            short_url.short_code = custom_code
        
        short_url.save()
        return short_url