from django.shortcuts import render, HttpResponse
from app.models import Contact
# for message
from django.contrib import messages
# this code block for your logic
import random 
from django.core.mail import send_mail
from django.conf import settings
  
# determines how many values 
# will be printed 

def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
# for showing message
        if len(name)<2 or len(email)<20 or len(phone)<10 or len(content)<4:
            messages.error(request, "Please fill the form correctly!")
        else:
            import random
            n = random.randint(100000,999999)
            contact = Contact(name=name, email=email, phone=phone, content=content,rand_id=n)
            contact.save()
            
            
            messages.success(request, "Your form has been submitted successfully! ")
            messages.success(request, "Your Order id " +str(n))
            send_mail_user(name, email, phone, content, n)
    return render(request, 'contact.html')
#this function will send mail to the customer with unique 6 digit order id
def send_mail_user(name, email, phone, content, n):
    message = ' Hello ' + name+'  \n  ' + 'Mobile Number: ' + phone +'  \n  ' +'Your order:'+ content +'  \n  ' + 'Your Order id number: '  + str(n)
    subject = 'Your order is confirmed, Your Order id is' + str(n)
    email_id = []
    email_id.append(email)
    send_mail(subject, message, settings.EMAIL_HOST_USER, email_id, fail_silently=False)

def self_mail(name, phone, content, n):
    message = 'We have a order of' + name