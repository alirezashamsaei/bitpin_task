from rest_framework import serializers
from .models import BlogPost, Rating
from django.contrib.auth.models import User
from django.db.models import Avg


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class RatingSerializer(serializers.ModelSerializer):
    # user = serializers.ReadOnlyField()
    class Meta:
        model = Rating
        fields = ['user', 'post', 'rating']

class RateSerializer(serializers.ModelSerializer):
    # user = serializers.ReadOnlyField()
    class Meta:
        model = Rating
        fields = ['post', 'rating']

class BlogPostSerializer(serializers.ModelSerializer):

    ratings_count = serializers.SerializerMethodField(method_name='get_ratings_count')
    ratings_avg = serializers.SerializerMethodField(method_name='get_ratings_avg')
    user_rating = serializers.SerializerMethodField(method_name='get_user_rating')

    class Meta:
        model = BlogPost
        fields = ['title', 'body','ratings_count', 'ratings_avg', 'user_rating']


    def get_ratings_count(self, instance):
        return instance.rating_count

    def get_ratings_avg(self, instance):
        return instance.average_rating
    
    def get_user_rating(self, instance):
        request = self.context.get('request')
        user = request.user
        try:
            user_rating = Rating.objects.get(user=user, post=instance)
            return user_rating.rating
        except:
            return None
