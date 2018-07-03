from django.conf.urls import url

from main import views

app_name = 'main'

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^index/$', views.index, name='index'),
    url(r'^social/$', views.social, name='social'),
]