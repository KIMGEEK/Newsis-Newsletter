from .models import Post, User

from .serializers import PostSerializer, UserSerializer

from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework import status



# Create your views here.

class PostViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = Post.objects.filter(index=0) # 기본적으로는 index가 0인 애들(메인페이지용)
        
        weeks = self.request.query_params.get('weeks', None) # weeks가 인자로 들어왔으면 값, 안 들어왔으면 None
        
        if weeks is not None: # 인자 들어옴(/post?weeks='2025-5-4')
            queryset = Post.objects.filter(weeks=weeks) # weeks가 '2025-5-4'인 애들

        return queryset
    

class UserViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    def list(self, request, *args, **kwargs):
        ip_addr = request.META.get('HTTP_X_FORWARDED_FOR')
        if ip_addr:
            ip_addr = ip_addr.split(',')[0]  # 첫 번째 IP가 실제 클라이언트 IP
        else:
            ip_addr = request.META.get('REMOTE_ADDR')
        print("Client IP:", ip_addr)

        ALLOWED_GET_IP = [
        '127.0.0.1',
        '172.23.0.1',
        ]

        if ip_addr not in ALLOWED_GET_IP:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        queryset = self.get_queryset()

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class DataViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer