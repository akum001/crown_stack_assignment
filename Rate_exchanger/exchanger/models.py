from django.db import models

# Create your models here.

class Currency(models.Model):
    currency_name = models.CharField(max_length = 50)
    currency_code = models.CharField(max_length = 10)

    def __str__(self):
        return self.currency_name
