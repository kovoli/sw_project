from django.shortcuts import render
from .models import Store
from sw_project import helpers


def store_list(request):
    store_list = Store.objects.all().order_by('title')
    stores = helpers.pg_records(request, store_list, 24)

    return render(request, 'stores/store_list.html', {'stores': stores})

