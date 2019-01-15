from django.db import models
from django.urls import reverse

class Page(models.Model):
    hadis = models.CharField(max_length=1000)
    kategori = models.CharField(max_length=20)

    def __str__(self):
        return self.hadis

    def get_post_url(self):
        return reverse('post_edit', kwargs={'pk': self.pk})    