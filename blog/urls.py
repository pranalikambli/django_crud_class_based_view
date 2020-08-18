from django.urls import path

from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name="home"),
    path('<slug:slug>', DetailedView.as_view(), name="post_detail_view"),
    path('blog/manage_post_list', ManagePostList.as_view(), name="manage_post_list"),
    path('blog/add_post', AddView.as_view(), name="add_post"),
    path('blog/edit_post/<int:pk>', EditView.as_view(), name="edit_post"),
    path('blog/delete_post/<int:pk>', DeletePostView.as_view(), name="delete_post"),
]