from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Photo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    caption = models.CharField(max_length=100, default=None, blank=False)
    photo = models.ImageField(upload_to="gallery")
    desc = models.TextField()

    def __str__(self):
        return str(self.id)


GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES,
                              blank=True, max_length=10)
    mobile = models.CharField(blank=True, max_length=20)
    address = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return str(self.id)
