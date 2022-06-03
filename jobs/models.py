from django.db import models
from tinymce.models import HTMLField

JOB_CATEGORY = (
    ("Human Resource","Human Resource"),
    ("Marketing","Marketing"),
    ("Customer Services","Customer Services"),
    ("Teaching & Education","Teaching & Education"),
    ("Sales & Communication","Sales & Communication"),
    ("Business Development","Business Development"),
    ("others","others")
)

JOB_NATURE = (
    ("Part Time","Part Time"),
    ("Full Time","Full Time"),
    ("Over Time","Over Time")
)

# Create your models here.
class Jobs(models.Model):
    job_title = models.CharField(max_length=500)
    job_cateagry = models.CharField(choices=JOB_CATEGORY,max_length=50,default="")
    job_nature = models.CharField(max_length=50,choices=JOB_NATURE,default='')
    job_salary = models.CharField(max_length=50)
    job_vacancy = models.IntegerField()
    job_logo = models.FileField(max_length=300,upload_to='jobs_logos/',null=True,default=None)
    job_address = models.CharField(max_length=500)
    job_qualifications = HTMLField(default='')
    job_description = HTMLField(default='')
    job_company = HTMLField(default='')

    def __str__(self):
        return self.job_title 
    
    