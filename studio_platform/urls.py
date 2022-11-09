from django.urls import path
from studio_platform import views

urlpatterns = [
    path('', views.PostView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('<slug:slug>', views.PostDetail.as_view(), name='post_detail'),
    path('post/', views.new_post, name='new_post'),
    path('student_gallery/', views.StudentUploadView.as_view(), name='student_gallery'),
    path('photo_detail/<int:pk>', views.ImageDetail.as_view(), name='image_detail'),
    path('<int:pk>/update_image/', views.UpdateImageView.as_view(), name='update_image'),
    path('<int:pk>/delete_image/', views.ImageDeleteView.as_view(), name='delete_image'),
    # path('edit_profile/', views.UserEditView.as_view(), name='edit_profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('create_profile/', views.ProfileCreateView.as_view(), name='create_profile'),
    path('profile/', views.ProfileDetail.as_view(), name='profile'),
    # path("post/edit/<int:pk>", views.UpdatePostView.as_view(), name="update_image"),
]