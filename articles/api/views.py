from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from .serializers import BlogSerializer
from articles.models import Article


class BlogListApiView(ListCreateAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = BlogSerializer
    queryset = Article.objects.order_by('-date_added')

    # def get(self, request, *args, **kwargs):
    #     articles = Article.objects.order_by('-date_added')
    #     print(articles)
    #     serializer = BlogSerializer(articles, many=True)
    #     return Response(serializer.data)

    # def post(self, request, *args, **kwargs):
    #     serializer = BlogSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save(author=request.user)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)