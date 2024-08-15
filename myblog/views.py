from django.shortcuts import render

def home(request):
    return(render(request,"home.html"))

def b1(request):
    return(render(request,"blog1.html"))
