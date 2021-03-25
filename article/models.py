from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=255, blank=False, null=True, verbose_name="Title")
    description = models.TextField(blank=False, null=True, verbose_name="Description")
    votes = models.IntegerField(default=0, blank=True, null=True, verbose_name="Votes")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", args=[self.pk])
