"""We have views here to handle signup and CRUD Operation for Blog """
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Comment
from .forms import PostForm
from .models import Post, Category
from django.db.models import Count
from django.http import HttpResponseForbidden
from django.contrib.auth.views import redirect_to_login


def home(request):
    posts = Post.objects.order_by('-created_at')
    categories = Category.objects.all()
    featured_post = Post.objects.annotate(num_likes=Count('likes')).order_by('-num_likes').first()
    return render(request, 'blog/home.html', {
        'posts': posts,
        'featured_post': featured_post,
        'categories' : categories
    })

def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('logged_out')
    return render(request, 'registration/home.html')

def logged_out_view(request):
    return render(request, 'registration/logged_out.html')

from django.contrib.auth.decorators import login_required

@login_required
def my_account(request):
    return render(request, 'blog/my_account.html', {'user': request.user})

def about(request):
    return render(request, 'blog/about.html')

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all().order_by('-created_at')

    if request.method == 'POST':
        # Handle comment submission
        if 'comment_submit' in request.POST:
            if request.user.is_authenticated:
                comment_body = request.POST.get('comment')
                if comment_body:
                    Comment.objects.create(post=post, author=request.user, body=comment_body)
                    return redirect('post_detail', pk=pk)
            else:
                return redirect_to_login(request.get_full_path())

        # Handle like toggle
        elif 'like_submit' in request.POST:
            if request.user.is_authenticated:
                if request.user in post.likes.all():
                    post.likes.remove(request.user)
                else:
                    post.likes.add(request.user)
                return redirect('post_detail', pk=pk)
            else:
                return redirect_to_login(request.get_full_path())

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments
    })

def category_posts(request, category_id):
    # Get the category based on the category_id
    category = get_object_or_404(Category, id=category_id)
    
    # Get all posts that are in the selected category
    posts_in_category = Post.objects.filter(categories__id=category.id).order_by('-created_at')

    return render(request, 'blog/category_posts.html', {
        'category': category,
        'posts': posts_in_category,
    })

@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk

    if request.user == comment.author:
        comment.delete()
        return redirect('post_detail', pk=post_pk)
    else:
        return HttpResponseForbidden("You are not allowed to delete this comment.")


def user_posts(request, username):
    posts = Post.objects.filter(author__username=username)
    return render(request, 'blog/user_posts.html', {'posts': posts, 'username': username})

def signup(request):
    """ Functionality for Signing Up"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    for field in form.fields.values():
        field.widget.attrs['class'] = 'form-control'

    return render(request, 'registration/signup.html', {'form': form})

@login_required
def post_new(request):
    """Create a New Post Here, Remember login is necessary """
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})

@login_required
def post_edit(request, pk):
    """Editing our Post Functionality"""
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form})

@login_required
def post_delete(request, pk):
    """Deleting the Post Functionality"""
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect('home')
    return render(request, 'blog/post_confirm_delete.html', {'post': post})
