from django.contrib import admin

# Register your models here.
from sweden.models import Token, Article


class TokenAdmin(admin.ModelAdmin):
    list_display = ['token_name', 'created_at']


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Token, TokenAdmin)



