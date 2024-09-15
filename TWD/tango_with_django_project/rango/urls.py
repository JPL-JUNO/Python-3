from django.urls import path
from rango import views

# 这里是处理所有除去 rango/ 的 url


urlpatterns = [path("", views.index, name="index")]

# URL 映射调用 Django 的 url() 函数，其第一个参数是正则表达式 ^$。这个正则表
# 达式匹配空字符串，因为 ^ 表示开头，$ 表示结尾，而且二者之间没有任何内容，所以只能匹配
# 空字符串。用户访问的 URL，只要匹配这个模式，Django 就会调用 views.index() 视图。你可能
# 觉得匹配空 URL 没有什么意义，那为什么要这样做呢？还记得吗，匹配 URL 模式时，只会考虑
# 原 URL 的一部分。Django 先使用项目的 URL 模式处理 URL 字符串（rango/），去掉 rango/ 部
# 分之后得到空字符。然后把空字符串传给 Rango 应用，交给 rango/urls.py 中的 URL 模式处理。

# 后面的 name 参数是可选
# 的，这里把它设为字符串 'index'。为 URL 命名的目的是反向解析 URL，即通过名称引用 URL
# 映射，而不直接使用 URL。
