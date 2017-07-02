from django.conf.urls import url
from . import views


urlpatterns = [
    # post views
    url(r'^$', views.post_list, name='post_list'),
    url(r'^(?P<post>[-\w]+)/$', views.post_detail, name='post_detail'),
    url(r'^category/(?P<category_slug>[\w-]+)/$', views.post_list, name='posts_by_category'),
    url(r'^tag/(?P<tag_slug>[\w-]+)/$', views.post_list, name='posts_by_tag'),
]