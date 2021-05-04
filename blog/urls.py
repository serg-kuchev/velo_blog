from django.urls import path, include

from blog.views import articles_list, post_view

urlpatterns = [
    path('', articles_list, name='articles'),
    path('ccc', post_view, name='post')
]