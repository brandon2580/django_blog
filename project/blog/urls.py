from django.urls import path

from . import views

urlpatterns = [
    path('', views.blog_index_view),
    path('create_blog/', views.create_blog_view)
]