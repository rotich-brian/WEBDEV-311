from django.urls import reverse
from django.db import models

# Create your models here.
class Course (models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})

