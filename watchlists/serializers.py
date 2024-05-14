from rest_framework import serializers
from .models import Watchlist, Stock

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['id', 'symbol', 'latest_price']

class WatchlistSerializer(serializers.ModelSerializer):
    stocks = StockSerializer(many=True, read_only=True)

    class Meta:
        model = Watchlist
        fields = ['id', 'user', 'symbol', 'stocks']
