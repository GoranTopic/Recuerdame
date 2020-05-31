from django.contrib import admin
from .models import Tribute, Comment
# Register your models here.


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

class adminTribute(admin.ModelAdmin):
    inline = [ CommentInline, ]


admin.site.register(Tribute, adminTribute)
admin.site.register(Comment)
