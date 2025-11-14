from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.http import HttpResponse
from blog.models import Post
def home(request):
    return HttpResponse("You visited the blog home page.")
def about(request):
    return HttpResponse("You visited the about page.")
def index(request):
    return HttpResponse("You visited the blog index page.")
def post(request):
    return HttpResponse("You visited the blog post page.")
def postid(request, post_id):
    return HttpResponse(f"You are viewing post number {post_id}.")
def render_index_template(request):
    return render(request, 'blog/index.html')
def post_detail(request, post_id):
    context={
        'post_id': post_id,
        'title':f'Blog Post #{post_id}',
        'author':'Aakarsh',
    }
    return render(request,'blog/post_detail.html',context)
def render_about_template(request):
    return render(request, 'blog/about.html')
def post_by_author(request, name):
    post = get_object_or_404(Post, author=name)
    return render(request, 'blog/post_det.html', {'post': post})
def user_blog(request):
    user=request.user
    context={
        'user':user
    }
    return render(request, 'blog/user_blog.html', context)