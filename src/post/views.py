from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.template.loader import get_template
from django.conf import settings

from .forms import ContactForm, QuoteForm
from .models import Portfolio, Services, Additional

def index(request):
    form = QuoteForm()
    context = {
        'title': 'Home',
        "form": form
    }
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        send_mail(
            'Free Quote Request Form', 
            'Hi my name is ' + name + '!..... ' + message + ' You can contact me back at: ' + email,  
            'frwebdesigns1@gmail.com', 
            ['football45353@gmail.com'],
            fail_silently=True
        )

        return render(request, 'thanks.html')

    return render(request, 'index.html', context)
    
def portfolio(request):
    portfolio = Portfolio
    context = {
        'title': 'Portfolio',
        'portfolio': portfolio.objects.all(),
    }
    return render(request, 'portfolio.html', context )

def service(request):
    service = Services
    additional = Additional
    context = {
        'title': 'Portfolio',
        'service': service.objects.all(),
        'additional': additional.objects.all()
    }
    return render(request, 'service.html', context )


def contact(request):
    form = ContactForm()
    context = {
        'title': 'Contact Me',
        "form": form
    }
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        service = request.POST.get("service")
        message = request.POST.get("message")

        send_mail(
            'Contact Form', 
            'Hi my name is ' + name + '!..... ' + message + ' You can contact me back at: ' + email, 
            'frwebdesigns1@gmail.com', 
            ['football45353@gmail.com'], 
            fail_silently=True
        )

        return render(request, 'thanks.html')

    return render(request, 'contact.html', context )

def thanks(request):
    context = {
        'title': 'Thank You',
    }
    return render(request, 'thanks.html', context )
