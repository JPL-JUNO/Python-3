from django.contrib import admin
from rango.models import Category, Page

# Register your models here.


class PageAdmin(admin.ModelAdmin):
    # 定制管理界面，访问 Page 模型时显示网页的分类、名称和 URL
    # "../../IMAGES/5-5.png"
    list_display = ("title", "category", "url")


admin.site.register(Category)
admin.site.register(Page, PageAdmin)
