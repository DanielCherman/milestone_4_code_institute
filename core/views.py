from django.shortcuts import render, redirect
from .forms import ContactForm

def Home(request):
    return render(request, 'core/index.html')

def ContactUsView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:Home')
    else:

        form = ContactForm()

    context = {
        'form': form,
    }
    return render(request, 'core/contactus.html', context)
