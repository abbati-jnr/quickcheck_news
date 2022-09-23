from django.db import models

# Create your models here.


class Base(models.Model):
    TYPES = (
        ('story', 'Story'),
        ('job', 'Job'),
        ('comment', 'Comment')
    )

    hacker_news_id = models.IntegerField(unique=True, blank=True, null=True)
    deleted = models.BooleanField(blank=True, null=True)
    type = models.CharField(choices=TYPES, max_length=10)
    by = models.CharField(max_length=50, blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    dead = models.BooleanField(blank=True, null=True)
    kids = models.JSONField(blank=True, null=True)

    class Meta:
        abstract = True
        ordering = ['-pk']


class NewsItem(Base):
    descendants = models.IntegerField(blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=250, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    parent = models.IntegerField(blank=True, null=True)
    parts = models.JSONField(blank=True, null=True)
