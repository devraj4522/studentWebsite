from django.shortcuts import render,get_object_or_404
from .models import Post


def index(request):
    post = Post.published.all()
    context = {'post': post}
    return render(request, 'blog/index.html', context)

def post(request,slug):
    post = get_object_or_404(Post, slug=slug)
    context = {'post': post}
    return render(request, 'blog/post.html', context)