from django.urls import path
from . import views
from .feeds import LatestPostsFeed


app_name = 'job_openings'


urlpatterns = [
    path('', views.index, name="Blog Home"),
    path('admit-card/', views.admit_card, name="Admit_card"),
    path('latest-job/', views.latest_job, name="Latest_job"),
    path('result/', views.result, name="Result"),
    path('jobs/<slug:slug>/', views.post_view, name="postView"),
    path('feed/', LatestPostsFeed(), name='post_feed'),

]