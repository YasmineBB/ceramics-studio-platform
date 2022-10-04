from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


POST_STATUS = ((0, 'Draft'), (1, 'Published'))

# Models

"""
model for uploading a post.
"""


class Post(models.Model):
    caption = models.CharField(max_length=200, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='posts')
    posted_on = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    image = CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices=POST_STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)

    class Meta:
        ordering = ['-posted_on']

    def __str__(self):
        return self.caption

    def number_of_likes(self):
        return self.likes.count()


