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
    path("The Most Anticipated Games of the Year",views.top03,name='top3'),
    path("Urban Farming: Transforming Cities into Thriving Green Spaces",views.blg,name='blg'),
    path("Top 10 Books to Read Before They're Adapted to Movies",views.top4,name='top4'),
    path("Indian Chess Prodigy Gukesh Dommaraju Becomes Youngest World Chess Champion",views.news,name='news'),
    path("An Overview of the Naan Muthalvan Scheme by the Tamil Nadu Government",views.news1,name='news1'),
    path("How 5G Technology is Changing Communication",views.news3,name='news3'),
    path("Plastic pollution and how to reduce it",views.blog3,name='blog3'),
    path("The Future of Renewable Energy: Advancing Towards a Sustainable World",views.blog4,name='blog4'),
    path("Exploring the Pros and Cons of Online Education: Flexibility, Accessibility, and Challenges",views.blog5,name='blog5'),
    path("10 Quick and Healthy Recipes for Busy Professionals: Easy Meals to Save Time and Stay Fit",views.top5,name='top5'),
    path("Cybersecurity Tips: How to Stay Safe and secure in online",views.blog6,name='blog6'),
    path("10 Simple Ways to Reduce Stress and Improve Mental Health",views.top6,name='top6'),
    path("5 Easy and Delicious Desserts Anyone Can Make at Home",views.top7,name='top7'),
    path("Wildlife Conservation: Protecting Nature for Future Generations",views.blog7,name='blog7'),
    path("The Truth About Dieting: Separating Myths from Facts for a Healthier Lifestyle",views.blog8,name='blog8'),
    path("How the Technology is massively Transforming Education in this 2025",views.blog9,name='blog9'),
    path("Vidaa Muyarchi Box Office Report: Record Breaker or Slow Starter?",views.blog10,name='blog10'),
    path("Chandrayaan-4 Mission Unveiled: ISRO's Bold Leap Toward Lunar Sample Return by 2028",views.blog11,name='blog11'),
    path("My honest feedback",views.test,name='test'),
    path("How Gen Z Is Transforming the Indian Storytelling Landscape Across Digital and Traditional Platforms",views.news4,name='news4'),
    path("SRH vs CSK Thriller Recap: Sunrisers Hyderabad Edge Past Chennai Super Kings in Last-Ball Nail-Biter",views.news5,name='news5'),
]
