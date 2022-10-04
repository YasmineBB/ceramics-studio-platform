from django.shortcuts import render
from django.views import generic
from .models import Post


# Views

class PostView(generic.ListView):
    model = Post
    queryset = Post.objects.order_by('-posted_on')
    temmplate_name = 'index.html'
    paginate_by = 6
