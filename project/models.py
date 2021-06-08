from django.db import models
from django.db.models.deletion import CASCADE

class Projects(models.Model):
    name = models.TextField(null=True)
    description = models.TextField(null=True)
    duration = models.TextField(null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
 

    
class Tasks(models.Model):
    name = models.TextField()
    description = models.TextField()
    start_date = models.TextField()
    end_date = models.TextField()
    project = models.ManyToManyField(Projects)




    def __str__(self):
        return self.name




