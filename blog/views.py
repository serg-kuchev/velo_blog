from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView

# Вариант регистрации на базе класса FormView
class MyRegisterFormView(FormView):
    # Указажем какую форму мы будем использовать для регистрации наших пользователей, в нашем случае
    # это UserCreationForm - стандартный класс Django унаследованный
    form_class = UserCreationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/login/"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "register.html"

    def form_valid(self, form):
        form.save()
        # Функция super( тип [ , объект или тип ] )
        # Возвратите объект прокси, который делегирует вызовы метода родительскому или родственному классу типа .
        return super(MyRegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(MyRegisterFormView, self).form_invalid(form)


def articles_list(request):
    template = 'catalog.html'

    ordering = Post.objects.all().order_by('-published_at')
    context = {
        'object_list': ordering
    }
    return render(request, template, context)


def post_view(request, pk):
    template = 'product.html'

    try:
        post = get_object_or_404(Post, pk)

    except ObjectDoesNotExist:
        post = None

    context = {
        'post': post
    }

    return render(request, template, context)
