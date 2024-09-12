from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import TextDocument
from .serializers import TextDocumentSerializer

class TextDocumentListView(LoginRequiredMixin, generics.ListAPIView):
    serializer_class = TextDocumentSerializer

    def get_queryset(self):
        return TextDocument.objects.filter(user=self.request.user)

class TextDocumentCreateView(LoginRequiredMixin, generics.CreateAPIView):
    serializer_class = TextDocumentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TextDocumentDetailView(LoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TextDocumentSerializer

    def get_queryset(self):
        return TextDocument.objects.filter(user=self.request.user)
