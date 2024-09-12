from django.contrib import admin
from .models import TextDocument

@admin.register(TextDocument)
class TextDocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'id')
    search_fields = ('title',)
    list_filter = ('user',)
    ordering = ('-id',)
