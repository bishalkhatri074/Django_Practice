from django.shortcuts import render
from .models import Post, Comment
from django.shortcuts import redirect

def articles(request):
    posts = Post.objects.filter(is_published=True).order_by("-created_date")

    ctx = {
        "posts": posts
    }

    return render(request, template_name="blog/blog_index.html", context=ctx)

def articles_comment(request):
    comments = Comment.objects.all()

    gtx ={
        "comments": comments
    }

    return render(request, template_name="blog/blog_comment_create.html", context=gtx)

def create_articles(request):

    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')
        user = request.user

        post = Post.objects.create(title=title, text=body, author=user)

        return redirect('blog_index')

    return render(request, template_name="blog/blog_create.html", context={})

def create_comment(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        comment = request.POST.get('comment')

        user = request.user

        comment= Comment.objects.create(email=email, comment_text=comment,  )
        return redirect('blog_index')

    return render(request, template_name="blog/blog_comment_create.html", context={})