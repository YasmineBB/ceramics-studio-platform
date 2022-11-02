from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from django.http import HttpResponseRedirect
from .models import Post, UserProfile
from .forms import PostForm, UploadForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from django.contrib import messages


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


# class GalleryView(generic.TemplateView):
#     template_name = "student_gallery.html"
    

class StudentUploadView(generic.ListView):
    model = Post
    form_class = PostForm()
    context_object_name = 'photos'
    template_name = "student_gallery.html"
    queryset = Post.objects.order_by("-created_on")
    paginate_by = 30


# class LoginView(generic.TemplateView):
#     template_name = "registration/login.html"


# class CreatePostView(generic.CreateView):  
#     model = Post
#     form_class = PostForm
#     template_name = "post.html"
#     success_url = reverse_lazy("home")

"""
User upload new post view
"""

@login_required(login_url='/accounts/login/')
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        post = form.save(commit=False)
        post.user = request.user
        messages.success(request, 'Upload successful!')
        post.save()
        # return redirect('/')
        return redirect('student_gallery')
    else:
        form = PostForm()
    return render(request, 'post.html', {'form': form})


def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)



# class ImageCreateView(CreateView):
#     model = Post
#     form_class = PostForm
#     template_name = 'post.html'
#     success_url = reverse_lazy('student_gallery')

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)


"""
User edit profile view
"""
# message for user who tries to access the page without being logged in ('please sign in first')

# @login_required(login_url='/accounts/login/')
class UserEditView(generic.UpdateView):
    form_class = UserChangeForm
    template_name = 'profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
        # messages.success(request, 'Upload successful!')
        # return redirect('home')