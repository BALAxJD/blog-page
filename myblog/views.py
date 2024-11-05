from django.shortcuts import render

def home(request):
    return(render(request,"home.html"))

def b1(request):
    return(render(request,"blog1.html"))

def b2(request):
    return(render(request,"blog2.html"))

def sp1(request):
    return(render(request,"sp1.html"))

def tour(request):
    return(render(request,"tour1.html"))

def clim(request):
    return(render(request,"clim1.html"))
