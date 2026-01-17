from django.contrib import admin
from .models import Categories, Blog

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'Category', 'auther', 'status', 'is_featured', 'created_at')
    list_filter = ('status', 'is_featured', 'Category', 'created_at')
    search_fields = ('id','title', 'short_description', 'blog_Body','status')
    list_editable = ('status', 'is_featured')


admin.site.register(Categories)
admin.site.register(Blog, BlogAdmin)