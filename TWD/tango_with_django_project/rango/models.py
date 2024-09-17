from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    # unique 是为了解决大小写问题，但是这会与 default 的值产生冲突
    slug = models.SlugField(default="")

    def save(self, *args, **kwargs):
        # 调用 slugify() 函数更新 slug 字段。
        # 只要分类名称变了，别名就随之改变。
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        # 用来修改显示的名称
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.title
