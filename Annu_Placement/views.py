from django.shortcuts import render
from jobs.models import Jobs
from contact.models import user_cv, user_enquiry

def home(request):
    job_data = Jobs.objects.reverse()[:4]

    return render(request,'index.html',{"job_data":job_data})

def searchview(request):
    keyboard = request.GET.get("keyboard")
    category = request.GET.get("category")
    location = request.GET.get("location")
    

    if request.method == 'GET':
        if keyboard  != '':
            job_data = Jobs.objects.filter(job_title__icontains=keyboard)
        elif category != None:
            job_data = Jobs.objects.filter(job_cateagry=category)
        elif location != None:
            job_data = Jobs.objects.filter(job_address=location)
        else :
            print('Not Found')
    return render(request,'job-search.html',{'job_data':job_data})

def about(request):
    return render(request,'about-us.html')

def jobsdetails(request,job_id):
    job_data = Jobs.objects.get(id=job_id)
    data = {
        'job_details':job_data
    }
    return render(request,'job-details.html',data)

def jobs(request):
    job_data = Jobs.objects.all()
    return render(request,'jobs.html',{'job_data':job_data})

def contact(request):
    return render(request,'contact-us.html')

def privacyPolicy(request):
    return render(request,'Privacy-Policy.html')

def terms_conditions(request):
    return render(request,'Terms&Condition.html')

def thanks(request):

    if request.method =='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('mobile')
        msg = request.POST.get('massage')
        if name != '' or email != '' or phone != '' or msg != '':
            user_data = user_enquiry( user_name=name, user_email=email, user_phone=phone, user_massage=msg)

            user_data.save()
    return render(request,'thanks.html')

def cv_feedback(request):
    if request.method =='POST':
        resume = request.POST.get('cv')

        user_data = user_cv(user_resume=resume)

        user_data.save()

    return render(request,'thanks.html')





