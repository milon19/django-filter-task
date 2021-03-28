from django.urls import path

from posts.views import PostListView, PostSearchView

app_name = 'posts'

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post_list'),
    path('search/', PostSearchView.as_view(), name='post_search'),
]
