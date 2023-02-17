from django.db import models

# Create your models here.

class Tasks(models.Model):
    title = models.CharField(max_length=500, unique=True, null=False, default="")

    def __str__(self):
        return f"{self.id}, {self.title}"
    