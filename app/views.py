from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import BlogPost

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('blog_list')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def blog_list(request):
    posts = BlogPost.objects.all().order_by('-timestamp')
    return render(request, 'blog_list.html', {'posts': posts})


def blog_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog_detail.html', {'post': post})


@login_required
def blog_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        BlogPost.objects.create(title=title, content=content, author=request.user)
        return redirect('blog_list')
    return render(request, 'blog_form.html')


@login_required
def blog_edit(request, pk):
    post = get_object_or_404(BlogPost, pk=pk, author=request.user)
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('blog_detail', pk=post.pk)
    return render(request, 'blog_form.html', {'post': post})


@login_required
def blog_delete(request, pk):
    post = get_object_or_404(BlogPost, pk=pk, author=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('blog_list')
    return render(request, 'blog_confirm_delete.html', {'post': post})
