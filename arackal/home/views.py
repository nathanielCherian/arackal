from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail

def index(request):
    get_request(request)
    return render(request, "home/index.html")

def plumbing(request):
    return render(request, "home/plumbing.html")

def heating(request):
    return render(request, "home/heating.html")

def appliances(request):
    return render(request, "home/appliances.html")



recipients = ['arackalcontact@gmail.com',]
def get_request(request):
    if(request.method == "POST"):
        name = request.POST.get("name", 'nil')
        number = request.POST.get("number", 'nil')
        email = request.POST.get("email", 'nil')
        message = request.POST.get("message", 'nil')

        email_message = f"""
        NAME:         {name}
        PHONE NUMBER: {number}
        EMAIL:        {email}

        MESSAGE: 
        {message}
        """

        send_mail(
            'REQUEST FROM ' + name,
             email_message,
            'arackalcontact@gmail.com',
            recipients,
            fail_silently=False,
        )



def send_email():
    send_mail(
        'New Request',
        'message',
        'arackalcontact@gmail.com',
        ['ngcherian2014@gmail.com'],
        fail_silently=False,
    )