from django.shortcuts import render
import django_filters
import datetime
# Create your views here.
from django.http import HttpResponse
def home(request):return HttpResponse('bonjour à tous')
def index(request):
    return render(request,'ind.html')
def chart(request):
    tab = dht.objects.all()
    s = {'tab': tab}
    return render(request ,'chart.html', s)
def ind(request):
    return render(request,'ind.html')
from django.shortcuts import render
# Create your views here.
from .models import dht


def dht11(request):

    tab = dht.objects.all()
    s = {'tab': tab}
    return render(request, 'tables.html', s)
def dhtjour(request):

    tab=dht.objects.filter(dt__gte=datetime.date.today())
    s = {'tab': tab}
    return render(request, 'test.html', s)

def dhjour(request):
    d=datetime.timedelta(days=3)
    tab = dht.objects.filter(dt__gte=d)
    s = {'tab': tab}
    return render(request, 'test.html', s)

def histor(request):
    time = datetime.datetime.now() - datetime.timedelta(days=7)
    tab = dht.objects.filter(dt__gte=time)
    s = {'tab': tab}
    return render(request, 'test.html', s)


def test(request):
    s={}
    return render(request, 'test.html', s)
import csv
def export_to_csv(request):

    response=HttpResponse(content_type='text/csv')
    writer=csv.writer(response)
    writer.writerow(['temperature','date'])

    for d in dht.objects.all().values_list('temp', 'dt'):
        writer.writerow(d)

    response['Content-Disposition']='attachement; filename="donne.csv"'
    return response