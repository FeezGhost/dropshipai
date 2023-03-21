from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Subscription(models.Model):
    product_key = models.CharField(max_length=100)
    price_key = models.CharField(max_length=100)
    date_created =models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    customer_key = models.CharField(max_length=100)
    subscription_id = models.CharField(max_length=100)
    isSubscribed = models.BooleanField(default=True)

    def __str__(self):
        return str(self.user.username) + str(self.date_created)
