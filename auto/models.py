from django.db import models

# Create your models here.

class PriceCar(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    img = models.CharField(max_length=100)
    currency = models.CharField(max_length=10)
    time_price = models.FloatField()
    when_time = models.CharField(max_length=50)
    fuel = models.CharField(max_length=50)
    day_price = models.FloatField()
    when_day = models.CharField(max_length=50)
    month_price = models.FloatField()
    when_month = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.id}: {self.title}'
