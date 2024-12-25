from django.shortcuts import render
from . import models
# Create your views here.
def login(request):
	return render(request, 'log.html')

def home(request):
	return render(request, 'index.html')

def slogin(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		email = request.POST.get('mail')
		passwd = request.POST.get('passwd')
		contact_form = models.Slogin(name=name, email=email, passwd=passwd)
		contact_form.save()
		return render(request, 'index.html')
		