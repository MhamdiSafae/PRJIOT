from . import views
from django.urls.conf import path
from appl import views
from appl import api , serializer

urlpatterns = [
    path('data/', views.dht11, name='Data'),
    path('', views.index, name='home'),
    path('dash/', views.ind, name='dashboard'),
    path('chart/', views.chart, name='chart'),
    path('t/', views.dhtjour, name='chart'),
    path('h/', views.histor, name='chart'),
    ##api
    path('api/list', api.Dlist, name='DHT11List'),
    # genericViews
    path('api/post', api.Dhtviews.as_view(), name='DHT_post'),
    path('csv/', views.export_to_csv, name='export_to_csv'),

]

