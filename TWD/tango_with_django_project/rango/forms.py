from django import forms
from rango.models import Page, Category

# 对 ModelForm 的子类来说，最重要的一点或许是定义表单对应的模型。这个信息通过嵌套的 Meta
# 类提供，把 model 属性设为目标模型。


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    # 嵌套的类，为表单提供额外信息
    class Meta:
        # 把这个 ModelForm 与一个模型连接起来
        model = Category
        fields = ("name",)


class PageForm(forms.ModelForm):
    title = forms.CharField(
        max_length=128, help_text="Please enter the title of the page."
    )
    url = forms.URLField(max_length=200, help_text="Please enter the URL of the page.")

    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Page
        # 我们要通过 fields 指定表单中包含哪些字段，或者通过 exclude 指定排除哪些字段。
        exclude = ("category",)
