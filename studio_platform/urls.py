from django.urls import path
from studio_platform import views

urlpatterns = [
    path('', views.PostView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('<slug:slug>', views.PostDetail.as_view(), name='post_detail'),
    path('post/', views.new_post, name='new_post'),
    path('student_gallery/', views.GalleryView.as_view(), name='student_gallery'),
    # path("post/", views.CreatePostView.as_view(), name="add_post"),
]