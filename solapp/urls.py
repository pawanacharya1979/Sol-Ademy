from django.conf.urls import url
from . import views

urlpatterns = [
       url(r'^$', views.home, name='home'),
       url(r'^about-us/$', views.about, name='about'),
       url(r'^news/$', views.news, name='news'),
       url(r'^gallery/$', views.gallery, name='gallery'),
       url(r'^contact-us/$', views.contactus, name='contactus'),
       url(r'^student-visa/$', views.studentvisa, name='studentvisa'),
       url(r'^course-fees-structure/$', views.coursefee, name='coursefee'),
       url(r'^class-for-language/$', views.classes, name='classes'),
       url(r'^visa-process/$', views.visaprocess, name='visaprocess'),
       ]
