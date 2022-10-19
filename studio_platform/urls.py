from django.urls import path
from studio_platform import views

urlpatterns = [
    path('', views.PostView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('<slug:slug>', views.PostDetail.as_view(), name='post_detail'),
    # path('post/', views.new, name='new'),
    # path("post/", views.CreatePostView.as_view(), name="add_post"),
]