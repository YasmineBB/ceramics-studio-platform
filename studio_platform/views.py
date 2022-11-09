from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post, UserProfile
from .forms import PostForm, UploadForm, UserForm, CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


"""
View for user to see blog posts.
"""


class PostView(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = 'post_detail.html'

"""
View for user to comment on blog posts.
"""


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = post.comment.filter(approved=True).order_by("-posted_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comment": comment,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = post.comment.filter(approved=True).order_by("-posted_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comment,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


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



"""
View for users to upload an image.
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
User create profile view.
"""


class ProfileCreateView(generic.CreateView):
    model = UserProfile
    form_class = UserForm
    template_name = 'create_profile.html'
    success_url = reverse_lazy('create_profile')
    
    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)


"""
View for user to see their profile.
"""


# class ProfileDetail(generic.DetailView):
#     model = UserProfile
#     template_name = 'profile.html'
#     context_object_name = 'profile'
    
#     def get_queryset(self):
#         user = self.request.user
#         return UserProfile.objects.filter(username=user)


"""
User edit profile view.
"""
# message for user who tries to access the page without being logged in ('please sign in first')

# @login_required(login_url='/accounts/login/')
# class UserEditView(generic.UpdateView):
#     form_class = UserChangeForm
#     template_name = 'edit_profile.html'
#     success_url = reverse_lazy('home')

#     def get_object(self):
#         return self.request.user
        # messages.success(request, 'Upload successful!')
        # return redirect('home')


"""
User view profile view
"""
# def userpage(request):
# 	user_form = UserForm(instance=request.user)
# 	profile_form = ProfileForm(instance=request.user.profile)
# 	return render(request=request, template_name="profile.html", context={"user":request.user, "user_form":user_form, "profile_form":profile_form })


# def profile(request):
#     if request.method == 'POST':
#         user_form = UpdateUserForm(request.POST, instance=request.user)
#         profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

#         if profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(request, 'Your profile is updated successfully')
#             return redirect(to='profile')
#     else:
#         user_form = UpdateUserForm(instance=request.user)
#         profile_form = UpdateProfileForm(instance=request.user.profile)

#     return render(request, 'templates/profile.html', {'profile_form': profile_form})



@login_required(login_url='/accounts/login/')
def edit_profile(request):
    if request.method == "POST":
        # profile = UserProfile.objects.get(username=request.user)
        user_form = UserForm(request.POST, request.FILES, instance=request.user.profile)
        print(request.POST)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile was successfully updated!')
        else:
            messages.error(request, 'Unable to complete request')
            print('form invalid')
        return redirect("edit_profile")
    user_form = UserForm(instance=request.user.profile)
    return render(request=request, template_name="edit_profile.html", context={"user": request.user, "user_form":user_form })

# class edit_profile(generic.UpdateView):
#     model = UserProfile
#     template_name = 'edit_profile.html'
#     fields = ['first_name', 'last_name', 'bio',]
    
#     def get_success_url(self):
#         edit_profile = self.kwargs['pk']
#         # post.user = request.user
#         return reverse_lazy('edit_profile', kwargs={'pk': edit_profile})


# @login_required(login_url='/accounts/login/')
# def create_profile(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST, request.FILES)
#         profile = form.save(commit=False)
#         profile.user = request.user
#         messages.success(request, 'Upload successful!')
#         post.save()
#         # return redirect('/')
#         return redirect('student_gallery')
#     else:
#         form = UserForm()
#     return render(request, 'profile.html', {'form': form})


"""
View to allow user to update make changes to their image post.
"""


class UpdateImageView(generic.UpdateView):
    model = Post
    template_name = 'update_image.html'
    fields = ['image', 'caption',]
    
    def get_success_url(self):
        post = self.kwargs['pk']
        # post.user = request.user
        return reverse_lazy('image_detail', kwargs={'pk': post})


"""
View to allow user to view an particular image.
"""


class ImageDetail(generic.DetailView):
    model = Post
    template_name = 'image_detail.html'
    context_object_name = 'photo'


"""
View to allow user to delete an image they have posted.
"""


class ImageDeleteView(generic.DeleteView):
    template_name = 'delete_image.html'
    model = Post
    success_url = reverse_lazy('student_gallery')