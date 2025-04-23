from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Article, ArticleImage, Category
from .forms import ArticleImageForm

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'slug')
    prepopulated_fields = {'slug': ('category',)}

admin.site.register(Category, CategoryAdmin)

class ArticleImageInline(admin.TabularInline):
    model = ArticleImage
    form = ArticleImageForm
    extra = 0

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'slug', 'main_page')
    inlines = [ArticleImageInline]
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Article, ArticleAdmin)
