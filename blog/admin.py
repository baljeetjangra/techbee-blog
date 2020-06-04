from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','created_on','updated_on']
    list_filter = ['created_on','updated_on']
    search_fields = ['title','content']
    prepopulated_fields = {'slug':('title',)}
    class Meta:
        model = Post
admin.site.register(Post,PostAdmin)