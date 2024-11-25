"""
URL configuration for blog_page project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myblog import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('Top 10 populated cities/',views.b1,name='blog1'),
    path('impact of Melting glaciers/',views.b2,name="blog2"),
    path('AI in medicine/',views.sp1,name="sp1"),
    path('World tallest building/',views.tour,name="tour"),
    path('Urbanization shaping Environment',views.clim,name="clim"),
    path('Top 10 Dynasty in world',views.top1,name='top1'),
    path("top 5 best eco-friendly innovations/",views.top2,name='top2'),
    path("The Most Anticipated Games of the Year",views.top3,name='top3'),
]
