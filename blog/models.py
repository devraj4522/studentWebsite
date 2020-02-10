from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


# Create your models here.


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (('draft', "Draft"), ('published', 'Published'))

    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=60)
    slug = models.SlugField(max_length=60, unique_for_date='publish', )
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=10, default='draft')
    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # Our custom manage

    def __str__(self):
        return "Post By - {} - on - {}".format(self.author, self.title)

    class Meta:
        ordering = ('-publish',)

    def get_absolute_url(self):
        return reverse('blog:post', args=[self.slug])