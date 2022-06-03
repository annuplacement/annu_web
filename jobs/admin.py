from django.contrib import admin
from jobs.models import Jobs

# Register your models here.
class jobs_Listing(admin.ModelAdmin):
    list_add = ('__All__')


admin.site.register(Jobs,jobs_Listing)