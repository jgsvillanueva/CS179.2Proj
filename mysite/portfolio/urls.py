from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from .models import Post
from . import views

urlpatterns = [
    url(r'^home/$', ListView.as_view(queryset=Post.objects.all().order_by("-created_on"),
        template_name="portfolio/blog.html")),
    url(r'^home/(?P<pk>[0-9]+)/$', DetailView.as_view(model = Post,
                                                template_name="portfolio/post.html")),
]
