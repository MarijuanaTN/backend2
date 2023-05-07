from django.db import models

# Create your models here.
class ForexData_Weekly(models.Model):
    timestamp = models.DateField()
    symbol = models.CharField(max_length=10)
    open_price = models.FloatField()
    high_price = models.FloatField()
    low_price = models.FloatField()
    close_price = models.FloatField()

    class Meta:
        db_table = 'api_forexdata_weekly'