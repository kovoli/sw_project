from django.shortcuts import render
from stores.models import Store
from blog.models import Post


def lists(request):
    stores = Store.objects.all().order_by('title')
    posts = Post.objects.all().order_by('-publish')[:3]

    return render(request, 'content.html', {'stores': stores, 'posts': posts})