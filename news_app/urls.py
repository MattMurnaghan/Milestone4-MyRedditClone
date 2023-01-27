from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('create_post/', views.CreatePost.as_view(), name='create_post'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('upvote/<slug:slug>', views.PostUpvote.as_view(), name='post_upvote'),
    path('delete/<slug:slug>', views.DeletePost.as_view(), name='delete_post'),
    path('update_post/<str:title>', views.UpdatePost.as_view(), name='update_post'),
]
