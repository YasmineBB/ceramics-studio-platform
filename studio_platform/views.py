from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponseRedirect
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy


# Views

class PostView(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


class AboutView(generic.TemplateView):
    template_name = "about.html"


# class LoginView(generic.TemplateView):
#     template_name = "registration/login.html"


# class CreatePostView(generic.CreateView):  
#     model = Post
#     form_class = PostForm
#     template_name = "post.html"
#     success_url = reverse_lazy("home")

def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        post = form.save(commit=False)
        post.user = request.user
        post.save()
        return redirect('/')
    else:
        form = PostForm()
    return render(request, 'post.html', {'form': form})