from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect
from .models import Post


# Views

class PostView(generic.ListView):
    model = Post
    queryset = Post.objects.order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6

class AboutView(generic.TemplateView):
    template_name = "about.html"