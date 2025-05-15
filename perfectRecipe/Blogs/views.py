from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Blog
from .serializers import BlogSerializer

@api_view(['GET'])
def get_all_blogs(request):
    blogs = Blog.objects.all().order_by('-created_at')
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_blog_by_id(request, pk):
    try:
        blog = Blog.objects.get(pk=pk)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)
    except Blog.DoesNotExist:
        return Response({'error': 'Blog not found'}, status=status.HTTP_404_NOT_FOUND)
