from django.shortcuts import render
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            return render(request, 'thankyou.html', {'name': contact.full_name})
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
