from django.db import models
from account.models import Account


class Lesson(models.Model):
    PLACE = [
        ('Oras', 'Oras'),
        ('Poligon', 'Poligon')
        ]
    CATEGORY = [
        ('A', 'A'),
        ('A1', 'A1'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D')
    ]

    student = models.ForeignKey(Account, on_delete=models.CASCADE)
    category = models.CharField(max_length=2, choices=CATEGORY)
    place = models.CharField(max_length=10, choices=PLACE, null=False)
    date_time = models.DateTimeField(null=False)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)