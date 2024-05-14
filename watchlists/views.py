from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Watchlist
from .serializers import WatchlistSerializer
import requests
from rest_framework.decorators import action
from rest_framework.response import Response



class WatchlistViewSet(viewsets.ModelViewSet):
    serializer_class = WatchlistSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Watchlist.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['get'])
    def fetch_stocks(self, request, pk=None):
        watchlist = self.get_object()
        stocks = watchlist.stocks.all()

        for stock in stocks:
            response = requests.get(f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={stock.symbol}&interval=1min&apikey=32VI0XO1484YPIAN')
            data = response.json()
            stock.latest_price = data['Time Series (1min)'][list(data['Time Series (1min)'].keys())[0]]['4. close']
            stock.save()

        serializer = self.get_serializer(watchlist)
        print(serializer.data)
        return Response({'stocks': serializer.data})    
