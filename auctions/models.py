from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Auction(models.Model):
    title = models.CharField(max_length=64)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='auctions')
    price = models.IntegerField()
    description = models.TextField()
    pix_url = models.URLField()


class Bid(models.Model):
    price = models.IntegerField()
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name='bids')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bids')


class Comment(models.Model):
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()


class Category(models.Model):
    title = models.CharField(max_length=16)
    auctions = models.ManyToManyField(Auction, blank=True, related_name="categories")


