from django.shortcuts import render

# Create your views here.
def login(request):
	return render(request,"login.html")
def cuenta(request):
	return render(request,"cuenta/cuenta.html")