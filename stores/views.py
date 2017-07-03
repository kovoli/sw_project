from django.shortcuts import render, get_object_or_404
from .models import Store
from sw_project import helpers


def store_list(request):
    store_list = Store.objects.all().order_by('title')
    stores = helpers.pg_records(request, store_list, 24)

    return render(request, 'stores/store_list.html', {'stores': stores})


def store_detail(request, store):
    store = get_object_or_404(Store, slug=store)

    return render(request, 'stores/store_detail.html', {'store': store})