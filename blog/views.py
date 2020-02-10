from django.shortcuts import render,get_object_or_404
from .models import Post


def index(request):
    post = Post.published.all()
    context = {'post': post}
    return render(request, 'blog/index.html', context)

def post(request,slug):
    posts = Post.published.all()
    post = get_object_or_404(Post, slug=slug)
    context = {'post': post, 'posts': posts}
    return render(request, 'blog/post.html', context)