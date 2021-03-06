from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.mail import EmailMessage

# Create your views here.


def home(request):
    return render(request, 'solapp/home.html')


def about(request):
    return render(request, 'solapp/about.html')


def news(request):
    return render(request, 'solapp/news.html')


def gallery(request):
    return render(request, 'solapp/gallery.html')


def contactus(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('Name')
            email = form.cleaned_data.get('Email')
            phone = form.cleaned_data.get('phone_number')
            subject = form.cleaned_data.get('subject')
            message = form.cleaned_data.get('Message')
            body = {'Name':name,'Email':email,'phone_number':phone,'subject':subject,'Message':message},

            email = EmailMessage(
                'Contact From',
                str(body),
                to=['pawanacharya1979@gmail.com']
            )
            email.send()
            messages.success(request, 'Thank You! for contacting us, we will get back to you soon.')
            return HttpResponseRedirect('/contact-us/')
    else:
        form = ContactForm()
    return render(request, 'solapp/contact.html', {'form': form})


def studentvisa(request):
    return render(request, 'solapp/studentvisa.html')


def coursefee(request):
    return render(request, 'solapp/coursefee.html')


def classes(request):
    return render(request, 'solapp/class.html')


def visaprocess(request):
    return render(request, 'solapp/visaprocess.html')
