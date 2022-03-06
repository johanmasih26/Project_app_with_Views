import uuid
from django.db import models

class Project(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, null=True, blank=True)
    demo_link = models.CharField(max_length=1000, null=True, blank=True)
    source_link = models.CharField(max_length=1000, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(default=0)
    vote_ratio = models.IntegerField(default=0)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                        primary_key=True, editable=False)


    def __str__(self):
        return self.title


class Review(models.Model):
    VOTE_TYPE = (
        ('up','up'),
        ('down','down')
    )

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='reviews')
    body = models.TextField(max_length=500, null=True, blank=True)
    value = models.CharField(max_length=50, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, 
                            primary_key=True,editable=True)

    def __str__(self):
        return self.value


class Tag(models.Model):

    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, 
                            primary_key=True,editable=True)


    def __str__(self):
        return self.name
















