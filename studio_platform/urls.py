from django.urls import path
from studio_platform import views

urlpatterns = [
    path('', views.PostView.as_view(), name='home'),
]
