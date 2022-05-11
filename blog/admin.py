from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('slug', 'created_on', 'updated_on')


admin.site.register(Post, PostAdmin)
