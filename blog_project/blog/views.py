from django.shortcuts import render

# Create your views here.
def home(req):
    return render(req, 'home.html')

def blog_JHL(req):
    return render(req, 'blog_JHL.html')

def blog_SSJ(req):
    return render(req, 'blog_SSJ.html')