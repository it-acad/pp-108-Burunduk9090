from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('get_user_full_name', 'get_book_name', 'created_at', 'plated_end_at', 'end_at')
    search_fields = ('user__first_name', 'user__last_name', 'book__name')
    list_filter = ('created_at', 'plated_end_at', 'end_at')

    fieldsets = (
        (None, {
            'fields': ('user', 'book')
        }),
        ('Дати', {
            'fields': ('created_at', 'plated_end_at', 'end_at')
        }),
    )

    readonly_fields = ('created_at',)

    def get_user_full_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
    get_user_full_name.short_description = 'User'

    def get_book_name(self, obj):
        return obj.book.name
    get_book_name.short_description = 'Book'
