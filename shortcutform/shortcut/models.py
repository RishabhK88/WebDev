from django.db import models
from django.db.models.constraints import CheckConstraint, UniqueConstraint

# Create your models here.
class formdeets(models.Model):
    name = models.CharField(max_length=100)
    rno = models.CharField(max_length=10)
    email = models.EmailField()
    branch = models.CharField(max_length=5)
    ans1 = models.CharField(max_length=100)
    ans2 = models.CharField(max_length=100)
    ans3 = models.CharField(max_length=100)
    ans4 = models.CharField(max_length=100)
    qualified = models.BooleanField(default=False)

    def __str__(self):
        return self.name