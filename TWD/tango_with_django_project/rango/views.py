from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from rango.models import Category, Page


# 一个函数就是一个视图
# def index(request):
#     return HttpResponse(
#         "Rango says hey there partner!<a href='/rango/about/'>About</a>"
#     )
def index(request):
    # 构建一个字典，作为上下文传给模板引擎
    # 注意，boldmessage 键对应于模板中的 {{ boldmessage }}

    category_list = Category.objects.order_by("-likes")[:5]

    page_list = Page.objects.order_by("-views")[:5]
    context_dict = {"categories": category_list, "pages": page_list}

    # content_dict = {"boldmessage": "Crunchy, creamy, cookie, candy, cupcake!"}

    # 返回一个渲染后的响应发给客户端
    # 为了方便，我们使用的是 render 函数的简短形式
    # 注意，第二个参数是我们想使用的模板
    return render(request, "rango/index.html", context=context_dict)


# 视图函数至少有一个参数，即一个 HttpRequest 对象，它也在 django.http 模块中。按约
# 定，这个参数名为 request，不过你可以根据自己的意愿随意使用其他名称。

# 视图必须返回一个 HttpResponse 对象。


def about(request):
    return HttpResponse("Rango says here is the about page.<a href='/rango/'>Home</a>")


def show_category(request, category_name_slug):
    # Django 应用中的视图函数必须至少有一个参数。
    # 这个参数通常命名为 request，通过它获取与 HTTP 请求有关的信息。
    # 如果 URL 中带有参数，必须为对应的视图函数声明额外的具名参数。

    # 创建上下文字典，稍后传给模板渲染引擎
    context_dict = {}

    try:
        # 能通过传入的分类别名找到对应的分类吗？
        # 如果找不到，.get() 方法抛出 DoesNotExist 异常
        # 因此 .get() 方法返回一个模型实例或抛出异常
        category = Category.objects.get(slug=category_name_slug)

        # 检索关联的所有网页
        # 注意，filter() 返回一个网页对象列表或空列表
        pages = Page.objects.filter(category=category)

        # 把得到的列表赋值给模板上下文中名为 pages 的键
        context_dict["pages"] = pages

        # 也把从数据库中获取的 category 对象添加到上下文字典中
        # 我们将在模板中通过这个变量确认分类是否存在
        context_dict["category"] = category
    except Category.DoesNotExist:

        # 没找到指定的分类时执行这里
        # 什么也不做
        # 模板会显示消息，指明分类不存在
        context_dict["category"] = None
        context_dict["pages"] = None
    return render(request, "rango/category.html", context_dict)
