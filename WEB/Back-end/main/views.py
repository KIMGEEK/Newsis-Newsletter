from .models import Post

from .serializers import PostSerializer, UserSerializer

from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework import status



# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserCreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = UserSerializer

    def create(self, request):
        category_arr = request.data['categories']
        category_dict = {'web': '0', 'ai': '0', 'game': '0'}

        for category in category_arr:
            category_dict[category] = '1'
        
        req = ""
        for val in category_dict.values():
            req += val
        mod_request = request
        mod_request.data['categories'] = req

        serializer = UserSerializer(data=mod_request.data)
        # serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
