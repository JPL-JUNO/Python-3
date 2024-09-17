from django.contrib import admin
from rango.models import Category, Page

# Register your models here.


class PageAdmin(admin.ModelAdmin):
    # 定制管理界面，访问 Page 模型时显示网页的分类、名称和 URL
    # "../../IMAGES/5-5.png"
    list_display = ("title", "category", "url")


class CategoryAdmin(admin.ModelAdmin):
    # 定制管理界面，在输入分类名称时自动填写别名
    # slug = models.SlugField(blank=True)
    # 更新模型，把 slug 字段设为允许空值
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
