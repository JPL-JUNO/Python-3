from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


# 一个函数就是一个视图
# def index(request):
#     return HttpResponse(
#         "Rango says hey there partner!<a href='/rango/about/'>About</a>"
#     )
def index(request):
    # 构建一个字典，作为上下文传给模板引擎
    # 注意，boldmessage 键对应于模板中的 {{ boldmessage }}
    content_dict = {"boldmessage": "Crunchy, creamy, cookie, candy, cupcake!"}

    # 返回一个渲染后的响应发给客户端
    # 为了方便，我们使用的是 render 函数的简短形式
    # 注意，第二个参数是我们想使用的模板
    return render(request, "rango/index.html", context=content_dict)


# 视图函数至少有一个参数，即一个 HttpRequest 对象，它也在 django.http 模块中。按约
# 定，这个参数名为 request，不过你可以根据自己的意愿随意使用其他名称。

# 视图必须返回一个 HttpResponse 对象。


def about(request):
    return HttpResponse("Rango says here is the about page.<a href='/rango/'>Home</a>")
