from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail

def index(request):
    get_request(request)
    return render(request, "home/i.html")

"""
def plumbing(request):
    get_request(request)
    return render(request, "home/plumbing.html")

def heating(request):
    get_request(request)
    return render(request, "home/heating.html")

def appliances(request):
    get_request(request)
    return render(request, "home/appliances.html")
"""


def plumbing(request):
    get_request(request)
    service = {
        "name":"Plumbing",
        "image":"home/images/plumbing.JPG",
        "services":[
            'Pressure Tests',
            'Backwater Valves', 
            'Video Inspections', 
            'Slab Leaks Repaired', 
            'Faucets repaired or Replaced', 
            'Backflow Preventer Installation',
            'All Types of Re-piping Services', 
            'Water Pressure Regulation Devices', 
            'Sump Pumps Installed and Serviced', 
            'Cold/Hot, Sever & Gas line location',
            'Water Heaters Repaired and Replaced', 
            'Slab leak and Water Detection Services',
            'Hot water recalculation pump Installation',
            'Thankless/tank water heater cleaning & Service.',
            'Underground Water and Drain Piping Repaired', 
            'Water Closets and Urinals Repaired or Replaced']
    }

    return render(request, "home/service-template.html", context=service)

def heating(request):
    get_request(request)
    service = {
        "name":"Heating",
        "image":"home/images/heating.JPG",
        "services":[
            'Water Heater', 
            'Violation Corrections', 
            'Wall Heaters – Installed and serviced']
    }

    return render(request, "home/service-template.html", context=service)

def appliances(request):
    get_request(request)
    service = {
        "name":"Appliances",
        "image":"home/images/appliances.JPG",
        "services":[
            'Cooking Range', 
            'Garbage Disposals', 
            'Water Filtration Systems', 
            'Refrigerators, Freezers', 
            'Ice Maker Lines Installed', 
            'Coffee maker lines Installed', 
            'Appliance Hookups, both Water and Gas', 
            'Dishwashers, Clothes Washers, Gas Dryers']
    }

    return render(request, "home/service-template.html", context=service)


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

