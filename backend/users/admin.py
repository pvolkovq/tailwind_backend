from django.contrib import admin
from django.utils.safestring import mark_safe
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'avatar_preview', 'username', 'email', 'first_name', 'last_name')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    
    def avatar_preview(self, obj):
        if obj.avatar:
            return mark_safe(f'<img src="{obj.avatar.url}" style="width: 50px; height: 50px; border-radius: 50%;" />')
        return 'No Avatar'

    avatar_preview.short_description = 'Avatar'