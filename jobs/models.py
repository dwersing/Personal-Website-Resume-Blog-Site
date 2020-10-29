from django.db import models


class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=45, default=None)
    summary = models.TextField(max_length=200)

    def __str__(self):
        return self.title