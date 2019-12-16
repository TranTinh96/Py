from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import BlogPost
from .forms import BlogPostModelForm


# Create your views here.
def index(request):
    return HttpResponse("Tran Tinh")


def blogPost(request, id):
    try:
        obj = BlogPost.objects.get(id=id)
    except:
        raise Http404
    template_name = 'blog_post_detail.html'
    content = {"object": obj}
    return render(request, template_name, content)


""""""""""""""""""""""""""""""""""""""
# CRUD -> Create Read Update Delete
# GET  -> Retrieve / List
# POST -> Create / Update /Delete
""""""""""""""""""""""""""""""""""""""


def blog_post_list_view(request):
    qs = BlogPost.objects.all()
    template_name = 'Blog/blog_post_list.html'
    content = {"object_list": qs}
    return render(request, template_name, content)


# @login_required
@staff_member_required
def blog_post_create_view(request):
    template_name = 'Blog/blog_post_create.html'
    form = BlogPostModelForm(request.POST or None)
    if form.is_valid():
        # Save Database
        form.save()
        # End Save
        form = BlogPostModelForm()
    content = {"form": form}
    return render(request, template_name, content)


def blog_post_detail_view(request):
    try:
        obj = BlogPost.objects.get(id=id)
    except:
        raise Http404
    template_name = 'Blog/blog_post_detail.html'
    content = {"object": obj}
    return render(request, template_name, content)


@staff_member_required
def blog_post_update_view(request,slug):
    try:
        obj = BlogPost.objects.get(slug=slug)
    except:
        raise Http404
    form = BlogPostModelForm(request.POST or None,instance=obj)
    print("-------------------------------------------------")
    print(form)
    if form.is_valid():
        form.save()
        form = BlogPostModelForm()
    template_name = 'Blog/blog_post_create.html'
    content = {"form": form , "title":obj.title}
    return render(request, template_name, content)


def blog_post_delete_view(request):
    try:
        obj = BlogPost.objects.get(id=id)
    except:
        raise Http404
    template_name = 'Blog/blog_post_delete.html'
    content = {"object": obj}
    return render(request, template_name, content)
