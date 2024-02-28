from django.shortcuts import render
from .models import User,Medicine,Prescription

def index(request):
    if request.method == "GET":
        users = User.objects.exclude(is_doc = True).all()
        doctors = User.objects.exclude(is_doc = False).get()
        return render(request,"online_medic/index.html",{"users":users,"doc":doctors})
    else:
        user_id = request.POST["user_id"]
        user = User.objects.get(id = user_id)
        doctors = User.objects.exclude(is_doc = False).get()
        meds = Medicine.objects.all()
        return render(request, "online_medic/patient.html", {"user":user,"doc":doctors,"meds":meds})
    
def pay(request):
    if request.method == "POST":
        meds = request.POST.getlist("medicine_id")
        elements = []
        patient = request.POST["cust_Id"]
        user = User.objects.get(id = patient)
        doctors = User.objects.exclude(is_doc = False).get()
        total_amount = 0
        for m_id in meds:
            each_med = Medicine.objects.get(id=m_id)
            elements.append([each_med.name,each_med.price])
            total_amount += each_med.price
        return render(request, "online_medic/payment.html", {"elements":elements, "user": user, "total":total_amount, "doc":doctors})
    else:
        return render(request, "online_medic/payment.html", {"names": [], "prices": [], "user": "krish"})
