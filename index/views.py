from django.shortcuts import render, redirect , get_object_or_404
from django.core.paginator import  Paginator,PageNotAnInteger, EmptyPage 
from Publication.models import *
import math
import random
from urllib.request import Request
import requests
from .forms import *
from django.views.decorators.http import require_http_methods
from django.core.mail import send_mail, BadHeaderError,mail_admins
from django.http import HttpResponse
from django.contrib import messages
import json
import environ
# Initialise environment variables
env = environ.Env()
environ.Env.read_env()



# Create your views here.

def HomeViews(request):
	stephaine = Publication.objects.all()[:6]
	content = {'step': stephaine}
	return render(request, 'index.html', content)

def profileview(request):

    return render(request, 'profile.html')	

def ContactViews(request):
	form = ContactForm(request.POST)
	if request.method == 'POST':
			if form.is_valid():
				form.save()
			return redirect ("index:contact")
	form = ContactForm()
	return render(request, 'contact.html')   

def ConsultingViews(request):
    if request.method == 'POST':
        f = ConsultionForm(request.POST)
        if f.is_valid():
            f.save()
            messages.add_message(request, messages.INFO, 'Feedback Submitted.')
            return redirect('index:consulting')
    else:
        f = ConsultionForm()
    return render(request, 'consulting.html')

def publicationViews(request):
	post = Publication.objects.all()
	paginator = Paginator(post, 3)
	page = request.GET.get('page')
	try:
		post = paginator.page(page)
	except PageNotAnInteger:
		# if is not an integer, deliver the first page
		post = paginator.page(1)
	except EmptyPage:
		# if the page is out of range deliver the last page
		post = paginator.page(paginator.num_pages) 
	content = {
		'public':post,
		'page':page,
	}
	return render(request, 'publications.html', content)	


def error(request):

    return render(request, '404.html')



def detailView(request, slug):
	single = Publication.objects.get(slug=slug)
	if request.method == 'POST':
		form = PaymentForm(request.POST)
		if form.is_valid():
			name =  form.cleaned_data['name']
			email = form.cleaned_data['email']
			book = form.cleaned_data['book']
			price = single.price
			phone = form.cleaned_data['phone']
			quantity = form.cleaned_data['quantity']
			address = form.cleaned_data['address']
			shipping = form.save(commit=False)
			shipping.bookname = request.user 
			shipping.save()
			return redirect(str(process_payment(name,email,phone,price)))
	else:
		form = PaymentForm()
	content={
		'single':single,
		'form':form
	}
	return render(request,'blog_details.html', content)                      

def process_payment(name,email,price,phone,):
     auth_token= env('SECRET_KEY')
     hed = {'Authorization': 'Bearer ' + auth_token}
     data = {
                "tx_ref":''+str(math.floor(1000000 + random.random()*9000000)),
                "amount":price,
                "currency":"KES",
                "redirect_url":"http://localhost:8000/callback",
                "payment_options":"card",
                "meta":{
                    "consumer_id":23,
                    "consumer_mac":"92a3-912ba-1192a"
                },
                "customer":{
                    "email":email,
                    "phonenumber":phone,
                    "name":name
                },
                "customizations":{
                    "title":"Supa Electronics Store",
                    "description":"Best store in town",
                    "logo":"https://getbootstrap.com/docs/4.0/assets/brand/bootstrap-solid.svg"
                }
                }
     url = ' https://api.flutterwave.com/v3/payments'
     response = requests.method(url, json=data, headers=hed)
     response=response.json()
     link=response['data']['link']
     return link

@require_http_methods(['GET', 'POST'])
def payment_response(request):
    status=request.GET.get('status', None)
    tx_ref=request.GET.get('tx_ref', None)
    print(status)
    print(tx_ref)
    return HttpResponse('Finished')
