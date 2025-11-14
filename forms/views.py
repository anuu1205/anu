from django.shortcuts import render
from .form import ContactForm  # make sure the filename is form.py

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            print(f"Received message from {name} ({email}): {message}")
            return render(request, 'forms/success.html', {'name': name})
    else:
        form = ContactForm()
    return render(request, 'forms/contact.html', {'form': form})
