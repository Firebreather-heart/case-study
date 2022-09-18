from django.urls import reverse
from django.db import models

# Create your models here.
class ExtManager(models.Manager):
    def get_queryset(self):
        return super(ExtManager, self).get_queryset().filter(status='ext')

class LocalManager(models.Manager):
    def get_queryset(self):
        return super(LocalManager, self).get_queryset().filter(status='loc')

class AllManager(models.Manager):
    def get_queryset(self):
        return super(AllManager, self).get_queryset().all()

class NewsObject(models.Model):
    status = models.CharField(max_length=20, choices=(('loc', 'LOCAL'),('ext','EXTERNAL')), default='ext')
    type = models.CharField(max_length=20, db_index=True, default='general' )
    url = models.URLField(max_length=100, blank=True, null=True)
    author = models.CharField(max_length=100,)
    body = models.TextField(max_length=10000, blank=True)
    title = models.CharField(max_length=100, db_index=True)
    added = models.DateTimeField(auto_now=True)
    ext = ExtManager() # nOte that Ext belongs to the external Api
    loc = LocalManager() #thiss is referring to locally created News
    entire = AllManager()

    def __str__(self) -> str:
        return self.title

    