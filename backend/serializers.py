from rest_framework import serializers
from .models import BlogPost

class blogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model=BlogPost
        fields='__all__'