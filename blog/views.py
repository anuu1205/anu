from django.shortcuts import render
from .models import Post
# Create your views here.

from django.http import HttpResponse
def home(request):
    return HttpResponse("Welcome to the blog homepage")
def post_detail(request,id):
    return HttpResponse(f"This is blog post numner {id}")
def home(request):
    return render(request,'blog/index.html')
def demo(request,post_id):
    context={
        'post_id':post_id,
        'title':f'Blog Post #{post_id}',
        'author':'anuu',
    }
    
    return render(request,'blog/post.html',context)
def indexhtml(request):
    return render(request,'blog/indexnew.html')

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

# Show one post by slug
def post_detail(request, slug):
    post = Post.objects.get(id=slug)
    return render(request, 'blog/post-details.html', {'post': post})