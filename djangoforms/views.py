from django.shortcuts import render
from .forms import ContactForm
# Create your views here.
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()  # Save to database
            name = contact.name    # Access saved instance
            print(f"Received message from {contact.name} ({contact.email}): {contact.message}")
            return render(request, 'forms/success.html', {'name': name})
    else:
        form = ContactForm()
    return render(request, 'forms/contact.html', {'form': form})

