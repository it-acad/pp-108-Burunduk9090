from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_book_authors', 'year_of_publication', 'date_of_issue')
    search_fields = ('name', 'authors__name', 'authors__surname')
    list_filter = ('id', 'name', 'year_of_publication')

    fieldsets = (
        ('Immutable Data', {
            'fields': ('name', 'year_of_publication', 'authors')
        }),
        ('Mutable Data', {
            'fields': ('description', 'count')
        }),
    )

    readonly_fields = ('date_of_issue',)

    def get_book_authors(self, obj):
        return ", ".join(f"{author.name} {author.surname}" for author in obj.authors.all())
    get_book_authors.short_description = 'Authors'
