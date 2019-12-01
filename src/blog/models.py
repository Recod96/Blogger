 
from django.db import models 
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Comment(models.Model):

    text = models.TextField()
    suspense = models.ForeignKey(User,on_delete=models.CASCADE)
    comment_date = models.DateTimeField(default=timezone.now())
    comment_update = models.DateTimeField(auto_now=True)




class Categorie(models.Model):

    title = models.CharField(max_length=10)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Tag(models.Model):

    text = models.CharField(max_length=10)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.text 

class PostParagraphs(models.Model):

    header = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(upload_to='static/blog/image/')
    
    def __str__(self):
        return self.header
    

class Post(models.Model):

    title = models.CharField(max_length=100) 
    image = models.ImageField(upload_to='static/blog/image/')
    post_date = models.DateTimeField(default=timezone.now())
    post_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    categories = models.ManyToManyField(Categorie)
    postparagraphs = models.ManyToManyField(PostParagraphs)
    comments = models.ManyToManyField(Comment)

    def getTags(self):
        return self.tags
        
    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-post_date',)

 

