
from django.db import models


PROJECTS = (
    ['Yulu', 'Yulu'],
    ['Ola', 'Ola'],
    ['Uber', 'Uber'],
)

CLIENTS = (
    ('Intel', 'Intel'),
    ('Bosch', 'Bosch'),
)

# Create your models here.
# SN, ProjectName, Client, Hours, Description, SUBMIT
class ProjectEntry(models.Model):
    project_name = models.CharField(max_length=10, choices=PROJECTS)
    client = models.CharField(max_length=10, choices=CLIENTS)
    hours = models.IntegerField()
    description = models.CharField(max_length=50)