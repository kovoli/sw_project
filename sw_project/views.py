from django.shortcuts import render
from stores.models import Store


def lists(request):
    stores = Store.objects.all().order_by('title')

    return render(request, 'content.html', {'stores': stores})