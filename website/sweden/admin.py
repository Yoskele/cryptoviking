from django.contrib import admin

# Register your models here.
from sweden.models import Token


class TokenAdmin(admin.ModelAdmin):
    list_display = ['token_name', 'created_at']






admin.site.register(Token, TokenAdmin)



