from django.db import models

from django.contrib.auth.models import User

from django.utils import timezone



statusChoices = [
    (0,'pending'),
    (1,'confirmed'),
    (2,'shipped'),
    (3,'delivered'),
    (4,'rejected'),
]

categories = [
    ('phones','phones'),
    ('laptops','laptops'),
    ('assesories','assesories'),
    ('sound','sound')
]


class ProfileInfo(models.Model):
    email = models.EmailField(default='', null=False, blank=False)
    phone = models.CharField(default='',null=False, blank=False, max_length=254)
    fullname = models.CharField(default='',null=False, blank=False, max_length=254)
    home_address = models.TextField(default='',null=True, blank=True, max_length=600)
    city = models.CharField(default='',null=False, blank=False, max_length=254)
    state = models.CharField(default='',null=False, blank=False, max_length=254)
    date_added = models.DateTimeField(default=timezone.now)
    cartItems = models.CharField(default='',null=False, blank=False, max_length=900)



class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    itemIDArr = models.CharField(default='',null=False, blank=False, max_length=900)
    itemTotalPrice = models.DecimalField(max_digits=10000000, decimal_places=2)
    hasPaid = models.BooleanField(default=False)
    deliveryStatus = models.IntegerField(default=0, choices=statusChoices)
    date_added = models.DateTimeField(default=timezone.now)
    
    
