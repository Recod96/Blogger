from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request ,'blog/index.html',{'title':'my blog titile' })


def login(request):
    print(request)
    return render(request ,'blog/index.html',{'title':'my blog titile' })
