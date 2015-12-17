from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    ACTIVE = 1
    PAST = 0
    CANCELLED = 2
    DONE = 3
    LOST = 4
    STATUS_CHOICES = (
        (PAST, 'Past'),
        (ACTIVE, 'Active'),
        (CANCELLED, 'Cancelled'),
        (DONE, 'Done'),
        (LOST, 'Lost'),
    )
    status = models.IntegerField(choices=STATUS_CHOICES,
                                      default=ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    