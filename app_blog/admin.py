from django.contrib import admin
from django.shortcuts import get_list_or_404

from .models import Article, ArticleImage, Category
from .forms import ArticleImageForm


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'slug',)
    prepopulated_fields = {'slug': ('category',)}
    fieldsets = (
        ('', {
            'fields': ('category', 'slug',),
        }),
    )

admin.site.register(Category, CategoryAdmin)

# ---------------------------------------------

class ArticleImageInline(admin.TabularInline):
    model = ArticleImage
    form = ArticleImageForm
    extra = 0
    fieldsets = (
        ('', {
            'fields': ('title', 'image',),
        }),
    )

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'slug', 'category', 'main_page',)
    inlines = [ArticleImageInline]
    multiupload_form = True
    multiupload_list = False
    prepopulated_fields = {"slug": ("title",)}
    raw_id_fields = ('category',)
    fieldsets = (
        ('', {
            'fields': ('pub_date', 'title', 'description', 'category', 'main_page',),
        }),
        ((u'Додатково'), {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('slug',),
        })
    )

    def delete_file(self, pk, request):
        '''Delete an image.'''

        obj = get_list_or_404(ArticleImage, pk=pk)
        return obj.delete()

admin.site.register(Article, ArticleAdmin)