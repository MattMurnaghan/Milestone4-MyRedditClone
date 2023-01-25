from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from autoslug import AutoSlugField

STATUS = ((0, "Under Review"), (1, "Published"))
CATEGORIES = (
    (0, 'Uncategorised'),
    (1, 'Tech'),
    (2, 'Dogs'),
    (3, 'Cars'),
)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = AutoSlugField(populate_from='title')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(max_length=300, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)
    upvotes = models.ManyToManyField(
        User, related_name='user_upvotes', blank=True)
    downvotes = models.ManyToManyField(
        User, related_name='user_downvotes', blank=True)
    approved = models.BooleanField(default=True)
    category = models.CharField(max_length=30, blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_upvotes(self):
        return self.upvotes.count()


class Comment(models.Model):
    # I want both of these fields to be autopopulated and linked
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    # -- || --
    name = models.CharField(max_length=80)
    created_on = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    # comments should be approved by default
    approved = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Comment {self.body} by {self.name}'
