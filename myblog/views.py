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

def top1(request):
    return(render(request,"top1.html"))

def top2(request):
    return(render(request,"top2.html"))

def top03(request):
    return(render(request,"top3.html"))

def blg(request):
    return(render(request,"blg.html"))

def top4(request):
    return(render(request,"top4.html"))

def news(request):
    return(render(request,"news1.html"))

def news1(request):
    return(render(request,"news2.html"))
