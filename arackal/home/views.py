from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail

def index(request):
    get_request(request)
    return render(request, "home/index.html")

def plumbing(request):
    get_request(request)
    return render(request, "home/plumbing.html")

def heating(request):
    get_request(request)
    return render(request, "home/heating.html")

def appliances(request):
    get_request(request)
    return render(request, "home/appliances.html")



recipients = ['arackalcontact@gmail.com', 'akbabu200@yahoo.com']
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

