from rest_framework import viewsets,permissions,status
from rest_framework.response import Response
from .models import BlogPost, Rating
from .serializers import BlogPostSerializer, RatingSerializer, UserSerializer,RateSerializer
from django.contrib.auth.models import User
from rest_framework.pagination import PageNumberPagination


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    pagination_class = PageNumberPagination

class RatingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Rating.objects.prefetch_related().all()
    serializer_class = RatingSerializer
    pagination_class = PageNumberPagination


class RateViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = RateSerializer

    def list(self,request):
        data = {"message": "Rate a post"}
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):

        
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
        
            try:
                # Rating.objects.get_or_create()
                r, created = Rating.objects.update_or_create(post_id=request.data.get('post'),user=request.user, defaults={
                    "rating":request.data.get('rating')
                })
                if created:
                    message = "rating created"
                else:
                    message = "rating updated."

                print(request.data.get('post'),request.data.get('rating'))
                data = {"stauts": "success", "message":message}
                return Response(data, status=status.HTTP_200_OK)
                
            except Exception as e:
                data = {"error": str(e)}
                return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)