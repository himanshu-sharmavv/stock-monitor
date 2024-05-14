from django.db import models
from django.conf import settings

class Watchlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    symbol = models.CharField(max_length=10)

class Stock(models.Model):
    watchlist = models.ForeignKey(Watchlist, on_delete=models.CASCADE, related_name='stocks')
    symbol = models.CharField(max_length=10)
    latest_price = models.DecimalField(max_digits=10, decimal_places=2)
