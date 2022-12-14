from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post, UserProfile
from .forms import PostForm, UserForm, CommentForm
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


"""
View for users to like user images.
"""


class PostLike(View):
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


"""
View for users to like posts.
"""


def ImageLike(request, pk):
    posts = get_object_or_404(Post, id=request.POST.get('photo_id'))
    if posts.likes.filter(id=request.user.id).exists():
        posts.likes.remove(request.user)
        liked = False
    else:
        posts.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('image_detail', args=[str(pk)]))


""""
View to display and be directed to about page.
"""


class AboutView(generic.TemplateView):
    template_name = "about.html"


"""
View to display student creations feed.
"""


class StudentUploadView(generic.ListView):
    model = Post
    form_class = PostForm()
    context_object_name = 'photos'
    template_name = "student_gallery.html"
    queryset = Post.objects.order_by("-created_on").filter(status=0)
    paginate_by = 30


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
        return redirect('student_gallery')
    else:
        form = PostForm()
    return render(request, 'post.html', {'form': form})


def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)


"""
View for user to create a profile.
"""


class ProfileCreateView(UserPassesTestMixin, LoginRequiredMixin,
                        generic.CreateView):
    model = UserProfile
    form_class = UserForm
    template_name = 'create_profile.html'
    success_url = reverse_lazy('edit_profile')

    def test_func(self):
        if hasattr(self.request.user, 'profile'):
            return False
        else:
            return True

    def form_valid(self, form):
        form.instance.username = self.request.user
        messages.success(self.request, 'Profile created successfully!')
        return super().form_valid(form)


"""
View for user to edit their profile.
"""


@login_required(login_url='/accounts/login/')
def edit_profile(request):
    if request.method == "POST":
        user_form = UserForm(request.POST, request.FILES,
                             instance=request.user.profile)
        print(request.POST)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile was successfully updated!')
        else:
            messages.error(request, 'Unable to complete request')
            print('form invalid')
        return redirect("edit_profile")
    try:
        user_form = UserForm(instance=request.user.profile)
        return render(request=request, template_name="edit_profile.html",
                      context={"user": request.user, "user_form": user_form})
    except:
        return redirect('create_profile')


"""
View to allow user to update make changes to their image post.
"""


class UpdateImageView(generic.UpdateView):
    model = Post
    template_name = 'update_image.html'
    fields = ['image', 'caption', ]

    def get_success_url(self):
        post = self.kwargs['pk']
        messages.success(self.request, 'Your changes have been saved!')
        return reverse_lazy('image_detail', kwargs={'pk': post})


"""
View to allow user to view an particular image from the student creations page.
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
