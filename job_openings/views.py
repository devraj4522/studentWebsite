from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Comment, Email, Link, Category
from .forms import CommentForm

# Create your views here.


def index(request):
    posts = Post.published.all()
    entery = Post.objects.filter(sub_category=3, status='published')
    admit_card = Post.objects.filter(sub_category=1, status='published')
    result = Post.objects.filter(sub_category=2, status='published')
    category = Category.objects.all()
    if request.method == "POST":
        email = request.POST['subscribe']
        title = 'Home Page Subscriber'
        subscriber = Email(email=email, post_title=title)
        subscriber.save()
    context = {'post': posts, 'class_category': category,
               'entery': entery, 'admit_card': admit_card, 'result': result}
    return render(request, 'job_openings/index.html', context)


def post_view(request, slug):
    post = get_object_or_404(Post, slug=slug)
    all_post = Post.published.all()
    link = post.links.all()
    comment = post.comments.all()
    if request.method == "POST":
        name = request.POST['Name']
        email = request.POST['Email']
        subject = request.POST['Subject']
        message = request.POST['Message']
        new_comment = Comment(name=name, email=email, subject=subject,
                              message=message, post=post)
        new_comment.save()
    context = {'post': post, 'all_post': all_post, 'link': link, 'comment': comment }
    return render(request, "job_openings/post.html", context)


def latest_job(request):
    latest_job = Post.objects.filter(sub_category=3, status='published')
    context = {'latest_job': latest_job}
    return render(request, 'job_openings/latest_job.html', context)


def admit_card(request):
    admit_card = Post.objects.filter(sub_category=1, status='published')
    context = {'admit_card': admit_card}
    return render(request, 'job_openings/admit_card.html', context)


def result(request):
    result = Post.objects.filter(sub_category=2, status='published')
    context = {'result': result}
    return render(request, 'job_openings/result.html', context)

