from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    ratings = models.ManyToManyField(User, through='Rating', related_name='ratings')

    def __str__(self) -> str:
        return f"{self.title}"
    
    @property
    def rating_count(self):
        return self.ratings.count()
    
    @property
    def average_rating(self):
        return self.ratings.aggregate(Avg('rating__rating')).get("rating__rating__avg", None)

class Rating(models.Model):
    class RatingValues(models.IntegerChoices):
        ZERO = 0
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RatingValues.choices)

    def __str__(self) -> str:
        return f"{self.user.username}: {self.post.title} ({self.rating})"
