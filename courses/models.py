from django.db import models
import os

class Course(models.Model):
    # course
    course_code = models.CharField(max_length=255, null=False)
    name = models.CharField(max_length=255, null=False)
    period = models.CharField(max_length=255, null=False)
    # image = ImageF


    def __str__(self):
        return "{}".format(self.name)


def upload_to_images(instance, filename):
    # Define the directory where the image will be uploaded
    upload_directory = "static/images"

    # Get the filename extension from the uploaded file
    extension = os.path.splitext(filename)[1]

    # Construct the final path using the model's primary key and the filename
    final_filename = f"{instance.pk}{extension}"
    return os.path.join(upload_directory, final_filename)

class Unit(models.Model):
    # course
    unit_code = models.CharField(max_length=255, null=False)
    name = models.CharField(max_length=255, null=False)
    period = models.CharField(max_length=255, null=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    images=models.ImageField(upload_to=upload_to_images, blank=True)


    def __str__(self):
        return "{} ({})".format(self.name, self.course)





