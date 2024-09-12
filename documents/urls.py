from django.urls import path
from .views import TextDocumentListView, TextDocumentCreateView, TextDocumentDetailView

urlpatterns = [
    path('documents/', TextDocumentListView.as_view(), name='document_list'),
    path('documents/create/', TextDocumentCreateView.as_view(), name='document_create'),
    path('documents/<int:pk>/', TextDocumentDetailView.as_view(), name='document_detail'),
]
