from django.db import models

# Create your models here.
class ModelWithFileField(models.Model):
    obj = models.FileField()