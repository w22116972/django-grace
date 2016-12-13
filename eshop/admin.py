from django.contrib import admin
from .models import Category, PhoneCase, Tag

@admin.register(PhoneCase)
class PhoneCaseAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

