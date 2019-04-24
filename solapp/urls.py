from django.conf.urls import url
from . import views

urlpatterns = [
       url(r'^$', views.home, name='home'),
       url(r'^about-us/$', views.about, name='about'),
       url(r'^contact/$', views.news, name='news'),
       url(r'^gallery/$', views.gallery, name='gallery'),
       url(r'^contact-us/$', views.contactus, name='contactus'),
       ]
