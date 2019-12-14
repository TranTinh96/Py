from django.urls import path

from .views import (index,blogPost ,blog_post_list_view,blog_post_create_view)

urlpatterns = [
    path('', index, name='index'),
    path('detail/<int:id>',blogPost),
    path('detail/',blog_post_list_view),
    path('create/',blog_post_create_view),
]