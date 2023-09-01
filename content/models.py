from django.db import models
from ckeditor.fields import RichTextField

import sys
sys.path.append("..")

from courses.models import Unit


class Topic(models.Model):
    # course
    topic_code = models.CharField(max_length=255, null=False)
    name = models.CharField(max_length=255, null=False)
    period = models.CharField(max_length=255, null=False)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    # image = ImageF


    def __str__(self):
        return "{} - {}".format(self.name, self.unit)




class Content(models.Model):
    # unit
    name = models.CharField(max_length=255, null=False)
    description = RichTextField()
    period = models.CharField(max_length=255, null=False)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    # image = ImageF


    def __str__(self):
        return "{}".format(self.name)





