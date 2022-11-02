from django import forms
from .models import Post, UserProfile
from allauth.account.forms import SignupForm, LoginForm


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('caption', 'image',)
        


# class CustomSignupForm(SignupForm):
#     username = forms.CharField(required=True)
#     email = forms.EmailField(required=True)
    # password = forms.PasswordInput(required=True)

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user
    

class EditProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('username', 'first_name', 'last_name', 'bio',)
        

class UploadForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('caption', 'image', 'description',)