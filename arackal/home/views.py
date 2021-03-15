from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail

def index(request):
    get_request(request)
    return render(request, "home/i.html")

def plumbing(request):
    get_request(request)
    return render(request, "home/plumbing.html")

def heating(request):
    get_request(request)
    return render(request, "home/heating.html")

def appliances(request):
    get_request(request)
    return render(request, "home/appliances.html")


@xframe_options_sameorigin
def faucet_background(request):
    return render(request, "home/background.html")


recipients = ['akbabu200@yahoo.com', 'arackalplumbing@gmail.com']
def get_request(request):
    if(request.method == "POST"):
        name = request.POST.get("name", 'nil')
        number = request.POST.get("number", 'nil')
        email = request.POST.get("email", 'nil')
        message = request.POST.get("message", 'nil')

        print(name, number, email, message)

        return
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

