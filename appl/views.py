import datetime
from django.db.models import Max, Min, Avg
from django.db.models.functions import Round
# Create your views here.
from django.http import HttpResponse


def index(request):

    tab=dht.objects.all().order_by('-id')[:5]
    max = dht.objects.all().aggregate(Max('temp'))
    listmax = list(max.items())
    maxt = listmax[0][1]
    print(maxt)

    min = dht.objects.all().aggregate(Min('temp'))
    listmin = list(min.items())
    mint = listmin[0][1]

    avg = dht.objects.all().aggregate(avg=Round(Avg('temp')))
    listavg = list(avg.items())
    avgt = listavg[0][1]

    last = dht.objects.last()
    first = dht.objects.last()
    coun = dht.objects.count()
    print(coun)
    s = {'tab': tab, 'maxt': maxt, 'mint': mint, 'avg': avgt, 'last': last, 'first': first, 'count': coun}
    return render(request, 'ind.html', s)


def chart(request):
    tab = dht.objects.all()
    s = {'tab': tab}
    return render(request, 'chart.html', s)


def ind(request):
    tab=dht.objects.all().order_by('-id')[:5]

    max= dht.objects.all().aggregate(Max('temp'))
    listmax=list(max.items())
    maxt=listmax[0][1]
    print(maxt)

    min=dht.objects.all().aggregate(Min('temp'))
    listmin = list(min.items())
    mint = listmin[0][1]

    avg = dht.objects.all().aggregate(avg=Round(Avg('temp')))
    listavg = list(avg.items())
    avgt = listavg[0][1]

    last = dht.objects.last()
    first = dht.objects.first()
    coun=dht.objects.count()
    print(coun)
    s = {'tab': tab, 'maxt': maxt, 'mint': mint, 'avg': avgt,'last':last,'first':first,'count':coun}
    return render(request, 'ind.html',s)


from django.shortcuts import render
# Create your views here.
from .models import dht


def dht11(request):
    tab = dht.objects.all()
    s = {'tab': tab}
    return render(request, 'tables.html', s)


def dhtjour(request):
    tab = dht.objects.filter(dt__gte=datetime.date.today())
    s = {'tab': tab}
    return render(request, 'test.html', s)

def dhtjourch(request):
    tab = dht.objects.filter(dt__gte=datetime.date.today())
    s = {'tab': tab}
    return render(request, 'chart.html', s)


def dhjour(request):
    d = datetime.timedelta(days=3)
    tab = dht.objects.filter(dt__gte=d)
    s = {'tab': tab}
    return render(request, 'test.html', s)


def histor(request):
    time = datetime.datetime.now() - datetime.timedelta(days=7)
    tab = dht.objects.filter(dt__gte=time)
    s = {'tab': tab}
    return render(request, 'test.html', s)


def historch(request):
    time = datetime.datetime.now() - datetime.timedelta(days=7)
    tab = dht.objects.filter(dt__gte=time)
    s = {'tab': tab}
    return render(request, 'chart.html', s)

def test(request):
    s = {}
    return render(request, 'test.html', s)


import csv


def export_to_csv(request):
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    writer.writerow(['temperature', 'date'])

    for d in dht.objects.all().values_list('temp', 'dt'):
        writer.writerow(d)

    response['Content-Disposition'] = 'attachement; filename="donne.csv"'
    return response
