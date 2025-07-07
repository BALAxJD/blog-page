from django.shortcuts import render
from rest_framework import generics
from .serializers import blogPostSerializer
from .models import BlogPost

class BlogPostListCreateView(generics.ListCreateAPIView):
    queryset=BlogPost.objects.all()
    serializer_class=blogPostSerializer

class BlogPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=BlogPost.objects.all()
    serializer_class=blogPostSerializer

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

def news3(request):
    return(render(request,"news3.html"))

def blog3(request):
    return(render(request,"blog3.html"))

def blog4(request):
    return(render(request,"blog4.html"))

def blog5(request):
    return(render(request,"blog5.html"))

def top5(request):
    return(render(request,"top5.html"))

def blog6(request):
    return(render(request,"blog6.html"))

def top6(request):
    return(render(request,"top6.html"))

def top7(request):
    return(render(request,"top7.html"))

def blog7(request):
    return(render(request,"blog7.html"))

def blog8(request):
    return(render(request,"blog8.html"))

def blog9(request):
    return(render(request,"blog9.html"))

def blog10(request):
    return(render(request,"blog10.html"))

def blog11(request):
    return(render(request,"blog11.html"))
def test(request):
    return(render(request,"test.html"))
def news4(request):
    return(render(request,"news4.html"))

def news5(request):
    return(render(request,"news5.html"))

def news6(request):
    return(render(request,"news6.html"))

def blog12(request):
    return(render(request,"blog12.html"))

def news7(request):
    return(render(request,"news7.html"))

def news8(request):
    return(render(request,"news8.html"))

def blog13(request):
    return(render(request,"blog13.html"))

def blog14(request):
    return(render(request,"blog14.html"))

def news9(request):
    return(render(request,"news9.html"))

def biog(request):
    return(render(request,"biog.html"))

def top8(request):
     return(render(request,"top8.html"))