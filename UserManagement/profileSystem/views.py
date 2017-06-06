from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the profile page")


def profileOther(request, id):
	return HttpResponse("Hello, you are on the profile of " + id + "!")

def createProfile(request):
	return HttpResponse("You are now creating a new profile!")