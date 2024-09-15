from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


# 一个函数就是一个视图
def index(request):
    return HttpResponse(
        "Rango says hey there partner!<a href='/rango/about/'>About</a>"
    )


# 视图函数至少有一个参数，即一个 HttpRequest 对象，它也在 django.http 模块中。按约
# 定，这个参数名为 request，不过你可以根据自己的意愿随意使用其他名称。

# 视图必须返回一个 HttpResponse 对象。


def about(request):
    return HttpResponse("Rango says here is the about page.<a href='/rango/'>Home</a>")
