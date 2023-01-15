from django.shortcuts import render
from . models import contact
from . forms import contactForm
from django.contrib import messages

def tea(request):
    return render(request,'home.html')


def about(request):
    return render(request,'about.html')


def contact_add(request):
    if request.method=='POST':
        e=request.POST['email']
        if contact.objects.filter(email=e).exists():
            messages.info(request,'Email already exists')
            return render(request,'contact.html')

        else :
            c=contactForm(request.POST)
            if c.is_valid():
                c.save()
                messages.success(request,"Successfully delivered message")
                return render(request,'contact.html')
            else:
                print("Invalid data")
    else:
        return render(request,'contact.html')

# Create your views here.
