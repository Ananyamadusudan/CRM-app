from django.db import models
from django.contrib.auth.models import User

from team.models import Team


class Lead(models.Model):
    NEW = 'new'
    CONTACTED = 'contacted'
    INPROGRESS = 'inprogress'
    LOST = 'lost'
    WON = 'won'

    CHOICES_STATUS = (
        (NEW, 'New'),
        (CONTACTED, 'Contacted'),
        (INPROGRESS, 'In progress'),
        (LOST, 'Lost'),
        (WON, 'Won'),
    )

    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'

    CHOICES_PRIORITY = (
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
    )
    team = models.ForeignKey(Team, related_name='leads', on_delete=models.CASCADE)
    company = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    website = models.CharField(max_length=255, blank=True, null=True)
    confidence = models.IntegerField(null=True, blank=True)
    estimated_value = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=25, choices=CHOICES_STATUS,
                              default=NEW)
    priority = models.CharField(max_length=10, choices=CHOICES_PRIORITY, default=LOW)
    created_by = models.ForeignKey(User, related_name='leads', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
