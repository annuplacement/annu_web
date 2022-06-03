from django.db import models

# Create your models here.
class user_enquiry(models.Model):
    user_name = models.CharField(max_length=300,default='',null=True)
    user_email = models.EmailField(max_length=500,default='',null=True)
    user_phone = models.CharField(max_length=50,default='',null=True)
    user_massage = models.TextField(default='',null=True)


    def __str__(self):
        return self.user_name


class user_cv(models.Model):
    user_resume = models.FileField(max_length=300,upload_to='user_cv/',null=True,default=None)

    def __str__(self):
        return self.user_resume
