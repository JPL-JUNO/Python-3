import os

# 导入 Django 模型之前要导入 django，
# 并把环境变量 DJANGO_SETTINGS_MODULE 设为项目的设置文件，
# 然后调用 django.setup()，导入 Django 项目的设置
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tango_with_django_project.settings")

import django

django.setup()
from rango.models import Category, Page


def populate():
    python_pages = [
        {
            "title": "Official Python Tutorial",
            "url": "http://docs.python.org/2/tutorial/",
        },
        {
            "title": "How to Think like a Computer Scientist",
            "url": "http://www.greenteapress.com/thinkpython/",
        },
        {
            "title": "Learn Python in 10 Minutes",
            "url": "http://www.korokithakis.net/tutorials/python/",
        },
    ]

    django_pages = [
        {
            "title": "Official Django Tutorial",
            "url": "https://docs.djangoproject.com/en/1.9/intro/tutorial01/",
        },
        {"title": "Django Rocks", "url": "http://www.djangorocks.com/"},
        {"title": "How to Tango with Django", "url": "http://www.tangowithdjango.com/"},
    ]
    other_pages = [
        {"title": "Bottle", "url": "http://bottlepy.org/docs/dev/"},
        {"title": "Flask", "url": "http://flask.pocoo.org"},
    ]

    cats = {
        "Python": {"pages": python_pages, "views": 128, "likes": 64},
        "Django": {"pages": django_pages, "views": 64, "likes": 32},
        "Other Frameworks": {"pages": other_pages, "views": 32, "likes": 16},
    }

    for cat, cat_data in cats.items():
        c = add_cat(cat, views=cat_data["views"], likes=cat_data["likes"])
        for p in cat_data["pages"]:
            add_page(c, p["title"], p["url"])

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f"- {str(c)} - {str(p)}")


def add_page(cat, title, url, views=0):
    # get_or_create() 方法检查数据库中有没有要创建的记录；如果没
    # 有，创建指定的记录；否则，返回那个模型实例的引用。
    # get_or_create() 方法返回一个元组 (object, created)。第一个元素是数据库中不存在记录
    # 时创建的模型实例引用。
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p


def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c


if __name__ == "__main__":
    print("Starting Rango population script...")
    populate()
