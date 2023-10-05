from django.contrib import admin
from .models import *

# Register your models here.

#
# class PostAdmin(admin.ModelAdmin):
#     model = Post
#     list_display = ('title', 'author', 'created_at')
#     filter_horizontal = ('tags',)
#     readonly_fields = ('created_at',)


admin.site.register(Post)