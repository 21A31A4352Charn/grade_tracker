from django.shortcuts import render,HttpResponse,redirect
from sendsms.message import SmsMessage

from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout as django_logout


from .models import *
from .test import getrollnumber,getdate,passwords,uppercase,forginkeys


from django.contrib import messages
from django.core.mail import send_mail


from django.shortcuts import render, redirect
from django.conf import settings




# Create your views here.
def login1(request):
    if request.method=="POST":
        username=request.POST.get("Username").upper()
        password=request.POST.get("password")
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            request.session['firstname']=request.user.first_name
            request.session['username']=request.user.username
            request.session['lastname']=request.user.last_name
            return redirect(data)
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')

def logins(request):
    return redirect(login1)

def data(request):
    first_name=request.session.get('firstname')
    user_name=request.session.get('username')
    last_name=request.session.get('lastname')
    s=mark.objects.all().filter(userName=user_name).values()
    print(s)
    m=(mark.objects.all().filter(userName=user_name).values_list('Mark'))
    sum=0
    count=0
    for i in m:
        sum=sum+i[0]
        count=count+1
    try:
        average=int(sum/count)
    except:
        average=0
    context={"first_name":first_name,"user_name":user_name,"last_name":last_name,"marks":s,"sum":sum,"count":count,"average":average}
    return render(request, 'marks.html',context)

def enter(request):
    if request.method=="POST":
        number=getrollnumber()
        date=getdate()
        for i in range(1,140):
                u=number[i][0]
                username=uppercase(u)
                dateofexam=date
                ma=str(number[i][1])
                mar=ma[8:10]
                if len(mar)==0:
                    marks=0
                else:
                    marks=int(mar)
                datas=mark(userName=username,dateOfExam=dateofexam,Mark=marks)
                datas.save()
                forginkeys(username)
        #mark.objects.all().delete()
        return HttpResponse("Success full saved")
    else:
        return redirect(login1)

def new(request):
     if request.method=="POST":
        return redirect(newsubmition)
     else:
        return redirect(newsubmition)

def newsubmition(request):
    if request.method=="POST":
        username=request.POST.get("username")
        name=request.POST.get("name")
        branch=request.POST.get("branch")
        email=request.POST.get("email")
        password=request.POST.get("password")
        v=passwords(username)
        if v==False:
            return HttpResponse("Use uppercase letters and must contain 10 characters")
        user=User.objects.create_user(username=username,first_name=name,last_name=branch,email=email,password=password)
        s=student(username=username)
        s.save()
        forginkeys(username)
        '''subject = 'Metaverse club'
        message = 'You have sussessfull created your account .Use same mail for reset your passwords'
        recipient = email
        send_mail(subject,message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)

        messages.success(request, 'Success!')
        m=SmsMessage(body="hello you have created an account", from_phone='8125977682', to='7842493132')
        m.send()

        print("SMS sent sussessfully")'''
        return redirect(login1)
    else:
        return render(request,'new.html')

def logout(request):
    if request.method=="POST":
        django_logout(request)
        return redirect(login1)
    else:
         return HttpResponse("You have login sussesfull")




'''def submit(request):
    if request.method=="POST":
        username=request.POST.get("usernames").upper()
        dateofexam=request.POST.get("dateofexames")
        marks=request.POST.get("markss")
        sub=mark(userName=username,dateOfExam=dateofexam,Mark=marks)
        sub.save()
        s=student(marks=username)
        return redirect(login1)
    else:
        return redirect(submit)'''