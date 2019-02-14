from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TimeStamp(models.Model):
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True

class List(TimeStamp):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="lists")
    date = models.DateField(auto_now=False, auto_now_add=False)
    completed = models.BooleanField(default=False)

    class Meta:
        unique_together = ('title', 'date', 'user', )

    def __str__(self):
        return self.title

class Task(TimeStamp):
    name = models.CharField(max_length=250)
    time_allocated = models.DurationField()
    time_remaining = models.DurationField()
    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name="tasks")
    category = models.CharField(max_length=20)
    completed = models.BooleanField(default=False)

    class Meta:
        unique_together = ('list', 'name', )

    def __str__(self):
        return self.name
