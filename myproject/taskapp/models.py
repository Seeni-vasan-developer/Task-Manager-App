from django.db import models

class Task(models.Model):
    priority_choices = [('High','high'),('Medium','Medium'),
                        ('Low','Low')]
    status_choices = [('Pending','Pending'),
                      ('In Progress','In Progress'),
                      ('Completed','Completed')]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    priority = models.CharField(max_length=15,choices=priority_choices)
    status = models.CharField(max_length=15,choices=status_choices)

    def __str__(self):
        return f"{self.title} ({self.priority}) - {self.status}"
    