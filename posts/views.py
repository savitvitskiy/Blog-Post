from django.shortcuts import render
from .models import Post, Comment
from .forms import CommentForm
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {
        "posts": posts,
    }
    return render(request, "index.html", context)


def post(request, pk):
    post = Post.objects.get(id=pk)
    comments = post.comments.filter(parent__isnull=True)
    form = CommentForm()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            parent_obj = None
            try:
                parent_id = int(request.POST.get("parent_id"))
            except:
                parent_id = None
            if parent_id:
                parent_qs = Comment.objects.filter(id=parent_id)
                if parent_qs.exists():
                    parent_obj = parent_qs.first()

            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post,
                parent=parent_obj,
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = CommentForm()

    context = {
        "post": post,
        "comments": comments,
        "form": CommentForm(),
    }
    return render(request, "post.html", context)
