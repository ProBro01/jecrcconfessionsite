from django.db import models

# Create your models here.
class confession(models.Model):
    name = models.CharField(max_length=20, default="virtual Thynos")
    discription = models.TextField()
    dateofpublish = models.DateField(auto_now_add=True)
    timeofpublish = models.TimeField(auto_now_add=True)