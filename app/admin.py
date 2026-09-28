from django.contrib import admin

from .models import User, Review, Zayavka

# Register your models here.

admin.site.site_header = 'Конференции.РФ | Админ панель'

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ['username', 'first_name', 'last_name', 'phone', 'email']

@admin.register(Zayavka)
class ZayavkaAdmin(admin.ModelAdmin):
    list_filter = ['name', 'date', 'status', 'payment']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_filter = ['created_at']