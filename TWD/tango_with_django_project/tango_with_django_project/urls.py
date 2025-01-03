"""
URL configuration for tango_with_django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

# path 使用的简单的，非正则的模式

from rango import views

urlpatterns = [
    path("", views.index, name="index"),
    path("rango/", include("rango.urls")),
    # 上面的映射把以 rango/ 开头的 URL 交给 rango 应用处理
    # re_path(r"^$", views.index, name="index"),
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
