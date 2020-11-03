#from django.urls import path
from django.conf.urls import url
from . import views
app_name = 'enque'
urlpatterns = [
#    path('', views.index, name='index'),
#    path('/', views.detail, name='detail'),
#    path('/results/', views.results, name='results'),
#    path('/vote/', views.vote, name='vote'),
    url(r'^$', views.index, name='index'),
	url(r'^(?P<pergs_id>[0-9]+)/$', views.detail, name='detail'),
	url(r'^(?P<pergs_id>[0-9]+)/results/$', views.results, name='results'),
	url(r'^(?P<pergs_id>[0-9]+)/vote/$', views.vote, name='vote'),
]

