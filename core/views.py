from django.shortcuts import render, redirect
from .forms import ContactForm


def home(request):
    form = ContactForm()
    return render(request, 'core/home.html', {
        'form': form,
        'description': 'Your restaurant description here',
        'services': ['Service 1', 'Service 2', 'Service 3'],
        'contact_info': 'Your contact info here'
    })


def about(request):
    return render(request, 'core/about.html', {
        'history': 'Your restaurant history here',
        'mission': 'Your mission statement here',
        'values': 'Your values here',
        'team': ['Member 1', 'Member 2', 'Member 3']
    })


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'core/contact.html', {'form': form})