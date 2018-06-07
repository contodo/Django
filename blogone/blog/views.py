from django.shortcuts import render,get_object_or_404
from .models import BlogArticles

# Create your views here.

def blog_title(request):
    blogs = BlogArticles.objects.all()
    return render(request,'blog/titles.html',{'blogs':blogs})

def blog_article(request,article_id):
    article = get_object_or_404(BlogArticles,id = article_id)
    return render(request,'blog/content.html',{'article':article})

def page_not_found(request):
    return render(request, '404.html')
