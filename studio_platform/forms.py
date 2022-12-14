from django import forms
from .models import Post, UserProfile, Comment
from allauth.account.forms import SignupForm, LoginForm


"""
Form for user to upload their work.
"""


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('caption', 'image',)
        

"""
Custom form to add first and last name to sign up form.
"""


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user


"""
Form for user to edit profile.
"""


class UserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'bio', 'profile_picture',)


"""
Form for user to comment on a post.
"""


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_body',)