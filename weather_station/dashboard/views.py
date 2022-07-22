from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import dashboard

# Create your views here.

@csrf_exempt
def home(request):
    if request.method == "POST":
        temp = request.POST.get('temp', None)
        hum = request.POST.get('hum', None)
        pres = request.POST.get('pres', None)
        alti = request.POST.get('alti', None)
        light = request.POST.get('light', None)
        print(f"{temp}--{hum}--{pres}--{light}")

        data = dashboard.objects.all().first()
        data.temperature = temp
        data.Humidity = hum
        data.pressure = pres
        data.altitude = alti
        data.lightInt = light
        data.save()
        return HttpResponse('<h1>Done</h1>')
    else:
        data = dashboard.objects.all().first()
        print(data.temperature)
        return render(request, 'dashboard/home.html', {"data": data})
    
def patial(request):
    data = dashboard.objects.all().first()
    return render(request, 'dashboard/patial.html', {"data": data})


