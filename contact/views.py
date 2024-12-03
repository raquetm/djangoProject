from django.shortcuts import render
from .models import ContactMessage

# Create your views here.
def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        ContactMessage.objects.create(name=name, email=email, message=message)
        return render(request, 'thankYou.html')
    return render(request, 'form.html')
