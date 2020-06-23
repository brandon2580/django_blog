from django.shortcuts import render, HttpResponse
from django.template import loader
from django.core.paginator import Paginator

from .models import Article

# Create your views here.


def blog_index_view(request):
    return render(request, 'blog/index.html')


def create_blog_view(request):
    articles = Article.objects.all()
    first_name = 'Brandon'
    last_name = 'Dalbec'

    if request.method == "POST":
        if "postAdd" in request.POST:
            print('postAdd was successful')
            title = request.POST["title"]
            author = request.POST["author"]
            content = request.POST["content"]
            CompleteArticle = Article(title=title, author=author, content=content)
            CompleteArticle.save()
    return render(request, 'blog/createBlog.html', context={'first_name': first_name, 'last_name': last_name, 'articles': articles})


def published_blogs_view(request):
    articles = Article.objects.all()
    template = loader.get_template('blog/publishedBlogs.html')
    context={'articles': articles}
    return HttpResponse(template.render(context, request))


def individual_blog_view(request):
    articles = Article.objects.all()
    paginator = Paginator(articles, 1) # Show 1 article per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/individualBlog.html', {'page_obj': page_obj})