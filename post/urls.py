from django.urls import path
from .views import post_list, post_details, new_post, post_edit, delete_post

urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/<int:pid>/', post_details, name = 'post_details'),
    path('post/add/', new_post, name = 'new_post'),
    path('post/<int:pid>/edit/', post_edit, name = 'edit_post'),
    path('post/<int:pid>/del/', delete_post, name = 'delete_post'),
]
