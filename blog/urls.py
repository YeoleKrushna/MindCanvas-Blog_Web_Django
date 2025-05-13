"""All blog app related Urls goes Here """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('logout/', views.user_logout, name='logout'),
    path('account/', views.my_account, name='my_account'),
    path('about/', views.about, name='about'),
    path('author/<str:username>/', views.user_posts, name='user_posts'),
    path('comment/<int:pk>/delete/', views.delete_comment, name='delete_comment'),
    path('category/<int:category_id>/', views.category_posts, name='category_posts'),
    path('logged_out/', views.logged_out_view, name='logged_out')
]