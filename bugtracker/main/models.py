from datetime import datetime
from django.db import models
from django.utils import timezone

class Bug(models.Model):
    bug_title = models.CharField(max_length = 200)
    bug_info = models.TextField()
    bug_published = models.DateTimeField('date published', default = datetime.now)

    def __str__(self):
        return self.bug_title
