from django.db import models
import uuid


class Parser(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    type = models.IntegerField()
    date_and_hour = models.DateTimeField()
    value = models.FloatField()
    cpf = models.CharField(max_length=11)
    credit_card = models.CharField(max_length=12)
    owner = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
