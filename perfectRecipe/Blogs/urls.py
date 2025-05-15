from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('lists/', views.get_all_blogs, name='get_all_blogs'),
    path('lists/<int:pk>/', views.get_blog_by_id, name='get_blog_by_id'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)