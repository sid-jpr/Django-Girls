# we're importing Django's function url and all of our views from the blog application
from django.conf.urls import url
from . import views

# we can add our first URL pattern
# we're now assigning a view called post_list to the ^$ URL – so only an empty string will match
# This pattern will tell Django that views.post_list is the right place to go if someone enters your website at
# the 'http://127.0.0.1:8000/' address
# name='post_list', is the name of the URL that will be used to identify the view

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
]
