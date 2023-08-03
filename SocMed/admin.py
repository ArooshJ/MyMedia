from django.contrib import admin

# Register your models here.
from .models import Post,Comment,Reply,Account

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(Account)