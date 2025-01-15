from django.contrib import admin
from .models import Author

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'patronymic')
    search_fields = ('name', 'surname')
    list_filter = ('id', 'name')
    fieldsets = (
        ('Основні Відомості', {
            'fields': ('name', 'surname', 'patronymic')
        }),
    )
