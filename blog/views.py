from django.shortcuts import render

from .forms import PostForm
from .models import Post


def create_post(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            Post.objects.create(content=form.cleaned_data['content'], user=request.user)
    return render(request, 'blog/posts/create_post.html', {"form": form})


def home(request):
    posts = Post.objects.all()  # QuerySet [1, 2, 3, 4, ....]
    #  Post.objects.filter(user=request.user, content="Hello")
    #  Post.objects.get(content="Hello")  object, instance   <- Get must return 1 instance, returned multiple instead
    #  Post.objects.get(id=2)
    return render(request, "blog/home.html", {"posts": posts})