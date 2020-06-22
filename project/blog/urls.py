from django.urls import path

from . import views

urlpatterns = [
    path('', views.blog_index_view),
    path('create_blog/', views.create_blog_view),
    path('published_blogs/', views.published_blogs_view),
    path(r'/individual_blog/(?P<id>\d+)/$', views.individual_blog_view),
]