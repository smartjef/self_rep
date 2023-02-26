from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import AdvocateSignUpForm
from .models import Contact, Service, Team, Profile
from allauth.account.views import SignupView


# Create your views here.
def index(request):
    services = Service.objects.all()
    teams = Team.objects.all()
    context = {
        'title': 'Home',
        'services': services,
        'teams': teams
    }
    return render(request, 'index.html', context)


def about(request):
    services = Service.objects.all()
    teams = Team.objects.all()
    context = {
        'title': 'About Us',
        'services': services,
        'teams': teams
    }
    return render(request, 'about.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        try:
            contact = Contact.objects.create(name=name, email=email, subject=subject, message=message)
            messages.success(request, 'Your message has been sent successfully')
            contact.save()
            return redirect('index')
        except IntegrityError:
            messages.warning(request, 'An error occured, your message could not be sent successfully')
            return redirect('contact')

    context = {
        'title': 'Contact Us'
    }
    return render(request, 'contact.html', context)


def services(request):
    services = Service.objects.all()
    context = {
        'title': 'Services',
        'services': services
    }
    return render(request, 'service.html', context)


class AdvocateSignUpView(SignupView):
    template_name = 'account/register.html'
    form_class = AdvocateSignUpForm

    def form_valid(self, form):
        field = form.cleaned_data.get("field")
        response = super().form_valid(form)
        Profile.objects.create(user=self.user, user_type="advocate", field=field)
        return response


class NormalSignUpView(SignupView):

    def form_valid(self, form):
        response = super().form_valid(form)
        Profile.objects.create(user=self.user)
        return response
