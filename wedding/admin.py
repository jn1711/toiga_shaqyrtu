from django.contrib import admin

from .models import RSVPResponse, Wish


@admin.register(RSVPResponse)
class RSVPResponseAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'attendance', 'created_at')
    list_filter = ('attendance', 'created_at')
    search_fields = ('full_name',)
    readonly_fields = ('created_at',)


@admin.register(Wish)
class WishAdmin(admin.ModelAdmin):
    list_display = ('name', 'message', 'created_at')
    search_fields = ('name', 'message')
    readonly_fields = ('created_at',)
