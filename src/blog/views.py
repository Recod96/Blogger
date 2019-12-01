from django.shortcuts import render , get_object_or_404
from .models import Post , Tag, Categorie,Comment
from django.core import serializers
# Create your views here.
 
def home(request):
    title = 'Home'
    posts = Post.objects.all()
    tags = Tag.objects.all()
    last_posts = Post.objects.all()[0:4]
    categorie = Categorie.objects.all()
 
    context = {
        'title':title,
        'posts': posts, 
        'postslast':last_posts, 
        'tags':tags, 
        'categories':categorie, 
    } 

    return render(request ,'blog/index.html',context)

def post_details(request,post_id):
    post = get_object_or_404(Post,pk=post_id)
    context = {
        'title':post.title,
        'post': post,  
    }
    return render(request,'blog/details.html',context)


def about(request):
    context = {
        'title':'Contact',
        'email':'rc-blogger@gmail.com',
    }
    return render(request ,'blog/contact.html',context)


 