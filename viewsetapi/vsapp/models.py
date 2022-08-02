from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=100)
    age = models.IntegerField()
    city = models.CharField(max_length=50)

    # def __str__(self):
    #     return f"{self.user_name} : age-{self.age} : city-{self.city}"
