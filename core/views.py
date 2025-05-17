from django.shortcuts import render,redirect
from .forms import ContactForm, DemoForm


def home(request):
    return render(request, 'core/home.html')

def products(request):
    return render(request, 'core/products.html')

def abaak(request):
    return render(request, 'core/abaak.html')

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')


def team_view(request):
    return render(request, 'core/team.html')


from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')  # success message can be added later
    else:
        form = ContactForm()
    return render(request, 'core/contact.html', {'form': form})


def demo(request):
    if request.method == 'POST':
        form = DemoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('demo')  # success message can be added later
    else:
        form = ContactForm()
    return render(request, 'core/demo.html', {'form': form})
