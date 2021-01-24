from django.db import models
from django.contrib.auth.models import User
from  django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager

# Create your models here.

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Profile_img = models.ImageField(upload_to='Profile_img/')
    bio = models.TextField(null=True,blank=True)

class Gategory(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title
 
class Post(models.Model):
    #user = models.OneToOneField(User, related_name='post_user', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    overview = models.TextField()
    #content = HTMLField(null=True,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    comment_count = models.IntegerField(default=0)
    view_count = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post/')
    categories = models.ManyToManyField(Gategory, related_name="post_category")
    featured = models.BooleanField(default=0)
    #previous_post = models.ForeignKey('self',related_name='previous', on_delete=models.SET_NULL, blank=True,null=True)
    #next_post = models.ForeignKey('self',related_name='next', on_delete=models.SET_NULL, blank=True,null=True)
    tag = TaggableManager()
    slug    = models.SlugField(blank=True,null=True)

   
    def save(self, *args, **kwargs):
        self.slug = self.title
        super(Post,self).save(*args, **kwargs)
        
    def __str__(self):
        return self.author.username
    def  get_absolute_url(self):
        return reverse('posts:post-detail', kwargs={'slug': self.slug})