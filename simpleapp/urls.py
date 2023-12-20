from django.urls import path
from .views import NewsList, NewsDetail, EditPost, DeletePost, CreatePost

urlpatterns = [
    path('', NewsList.as_view()),
    path('<int:pk>', NewsDetail.as_view()),
    path('<int:pk>/edit', EditPost.as_view()),
    path('<int:pk>/delete', DeletePost.as_view()),
    path('create/', CreatePost.as_view, name='post_create')
]