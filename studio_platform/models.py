from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


POST_STATUS = ((0, 'Draft'), (1, 'Published'))

# Models

"""
Model for uploading a post.
"""


class Post(models.Model):
    caption = models.CharField(max_length=200, unique=False)
    slug = models.SlugField(null=False, unique=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='posts')
    created_on = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    image = CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices=POST_STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.caption

    def number_of_likes(self):
        return self.likes.count()


"""
Model for commenting on a post.
"""


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comment')
    name = models.CharField(max_length=50)
    comment_body = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-posted_on']

    def __str__(self):
        return f'Comment {self.comment_body} by {self.name}'


# class StudentUpload(models.Model):
#     caption = models.CharField(max_length=50)
#     description = models.TextField(max_length=500)
#     posted_on = models.DateTimeField(auto_now_add=True)

"""
User profile model
"""

class UserProfile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.TextField(max_length=200)
    profile_picture = CloudinaryField('image')
    
    # def __str__(self):
    #     return self.username
