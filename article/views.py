from django.shortcuts import render, redirect, get_object_or_404
from .forms import ArticlePostForm, CommentForm
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import Article, Comment
from django.views.decorators.http import require_POST
from django.utils import timezone
from users.models import User


# Create your views here.
def article_out(request):
    return render(request, 'article/article.html')


def article_list(request):
    articles = Article.objects.all()
    return render(request, 'article_list.html', {'articles': articles})


@login_required(login_url='/users/login')
@csrf_exempt
def article_post(request):
    user = User.objects.get(username=request.user.username)
    if request.method == "POST":
        article_post_form = ArticlePostForm(request.POST)
        if article_post_form.is_valid():
            # cd = article_post_form.cleaned_data
            try:
                new_article = Article()
                # new_article=Article.objects.create_article(title,content)
                # new_article = article_post_form.save(commit=False)
                author = user
                new_article.author = author
                title = request.POST.get('title', None)
                content = request.POST.get('content', None)
                new_article.title = title
                new_article.content = content
                new_article.save()
                return redirect('article:article_list')
            except:
                return HttpResponse("2")
    else:
        article_post_form = ArticlePostForm()

        return render(request, "article/article.html",
                      {"article_post_form": article_post_form})

@login_required(login_url='/users/login/')
def article_detail(request, id):
    article = Article.objects.get(id=id)
    user = User.objects.get(username=request.user.username)
    if request.method == "POST":
        comment = request.POST.get('comment', None)
        # article_id = request.POST.get('article_id', None)
        new_comment = Comment()
        new_comment.article = article
        new_comment.body = comment
        new_comment.commentator = user
        new_comment.save()
    else:
        pass
    return render(request, 'article/article_detail.html', {'article': article, })


@csrf_exempt
@require_POST
@login_required(login_url='/users/login/')
def like_article(request):
    article_id = request.POST.get("id")
    action = request.POST.get("action")
    if article_id and action:
        try:
            article = Article.objects.get(id=article_id)
            if action == "like":
                article.users_like.add(request.user)
                return HttpResponse("1")
            else:
                article.users_like.remove(request.user)
                return HttpResponse("2")
        except:
            return HttpResponse("no")
