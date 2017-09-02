from django.db import models


class Link(models.Model):
    url = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.url

