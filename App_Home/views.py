from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect,redirect

def home(request):
    return redirect("App_Blog:blog_list")
