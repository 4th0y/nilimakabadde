from django.contrib import admin

from .models import Memory, Message, SiteConfig


@admin.register(SiteConfig)
class SiteConfigAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Hero", {"fields": ("friend_name", "hero_tagline")}),
        ("Letter", {"fields": ("letter_title", "letter_body")}),
        ("Music", {"fields": ("spotify_embed_url",)}),
    )

    def has_add_permission(self, request):
        # Only ever allow one row.
        return not SiteConfig.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Memory)
class MemoryAdmin(admin.ModelAdmin):
    list_display = ("caption", "date_label", "order")
    list_editable = ("order",)
    ordering = ("order", "id")


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("name", "message", "color", "approved", "created_at")
    list_editable = ("approved",)
    list_filter = ("approved", "color")
    search_fields = ("name", "message")
