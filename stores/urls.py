from django.conf.urls import url
from . import views


urlpatterns = [
    # post views
    url(r'^$', views.store_list, name='store_list'),
]