from django.urls import path
from . import views

urlpatterns = [
    path('lists/', views.get_all_blogs, name='get_all_blogs'),
    path('lists/<int:pk>/', views.get_blog_by_id, name='get_blog_by_id'),
]
