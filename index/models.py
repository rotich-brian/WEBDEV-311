from django.urls import reverse
from django.db import models

# Create your models here.
class Course (models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', default='img1.png')


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("course_detail", kwargs={"pk": self.pk})

