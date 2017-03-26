from django.db import models
from django.contrib.auth.models import User

class Trader(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	customer_id = models.CharField(max_length=200)
	account_ids = models.CharField(max_length=200)

