from django.urls import path
from .views import BoardListView, TopicListView, ThreadListView, CommentCreateView
from . import views


urlpatterns = [
    path('', BoardListView.as_view(), name='forum-home'),
    path('board/<int:pk>/', TopicListView.as_view(), name='forum-topics'),
    path('board/<int:pk>/<int:pk2>/', ThreadListView.as_view(), name='forum-thread'),
    path('board/<int:pk>/<int:pk2>/new_post/', CommentCreateView.as_view(), name='thread-new-post'),
]