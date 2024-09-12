from rest_framework import serializers
from .models import TextDocument

class TextDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextDocument
        fields = ['id', 'title', 'content']
