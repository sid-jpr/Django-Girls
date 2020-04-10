from django.shortcuts import render
# include the model we have written in models.py
# dot before models means current directory or current application. Both views.py and models.py are in the same directory.
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
# To create a new Post form, we need to call PostForm() and pass it to the template
from .forms import PostForm
from django.shortcuts import redirect

def post_list(request):
    # we want published blog posts sorted by published_date
    # post - name of the QuerySet
    posts = Post.objects.all()
    # In the render function we have one parameter request (everything we receive from the user via the Internet)
    # and another giving the template file ('blog/post_list.html'). The last parameter, {}, is a place in which we
    # can add some things for the template to use.
    return render(request, 'blog/post_list.html', {'posts': posts})

# we created a function (def) called post_list that takes request and return a function render that will render
# (put together) our template blog/post_list.html

def post_detail(request, pk):
    # In case there is no Post with the given pk, it will display much nicer page, the Page Not Found 404 page.
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            # commit=False means that we don't want to save the Post model yet – we want to add the author first
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            # immediately go to the post_detail page for our newly created blog post
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
