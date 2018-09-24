from django.shortcuts import render
from .models import *

def index(request):
    if request.method == "POST":
        reference_id = request.POST.get("reference_id")
        name = request.POST.get("name")
        address = request.POST.get("address")
        amount = request.POST.get("amount")
        trns_type = request.POST.get("trns_type")
        status="Initiated/Processing/Failed"
        c = Employee(reference_id,name,address,amount,trns_type,status)
        c.save()
        res = Employee.objects.filter()


        return render(request,"index.html",{"user_details":res})
    else:
        return render(request, "index.html")


