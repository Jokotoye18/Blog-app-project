from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.reverse import reverse
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated
from .permissions import IsOwnerOrReadOnly
from rest_framework import status
from .serializers import BlogSerializer, ContactSerializer, SubscribeSerializer
from articles.models import Article


class ApiRoot(APIView):
    def get(self, request, *args, **kwargs):
        return Response({
            'read-docs': reverse('schema-redoc', request=request),
            'blog-list': reverse('blog-api-list', request=request)
        })

class BlogListApiView(ListAPIView):
    permission_classes = [AllowAny, ]
    pagination_class = PageNumberPagination
    serializer_class = BlogSerializer
    queryset = Article.objects.all()
    filter_backends = [SearchFilter, OrderingFilter,]
    search_fields = ['title', 'body']
    ordering_fields = ['title', 'author__username', 'date_added']

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)
        
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

class BlogDetailApiView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly, ]
    queryset = Article.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'slug'
    lookup_url_kwarg='slug'

class ContactApiView(CreateAPIView):
    permission_classes = [AllowAny,]
    serializer_class =  ContactSerializer
    # def post(self, request, *args, **kwargs):
    #     serializer = ContactSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class SubscribeApiView(CreateAPIView):
    permission_classes = [AllowAny,]
    serializer_class = SubscribeSerializer