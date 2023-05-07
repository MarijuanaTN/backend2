from django.db import models




class ForexData(models.Model):
    timestamp = models.DateTimeField()
    symbol = models.CharField(max_length=10)
    bid_price = models.FloatField()
    ask_price = models.FloatField()
    exchange_rate = models.FloatField()



