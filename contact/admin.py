



from django.contrib import admin
from contact.models import user_cv, user_enquiry
# Register your models here.

class User_enquiry(admin.ModelAdmin):
    list_display = ("user_name","user_email","user_phone","user_massage")

admin.site.register(user_enquiry,User_enquiry)


class User_cv(admin.ModelAdmin):
    list_display = ("user_resume",)


admin.site.register(user_cv,User_cv)