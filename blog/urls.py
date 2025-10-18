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
from django.urls import path,include
from backend import views
from backend.views import github_webhook

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('backend.urls')),
    path('webhook', github_webhook),
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
    path("Why Gen Z Might Be the Last Generation to Truly Care About Digital Privacy in a Hyperconnected World",views.news6,name='news6'),
    path("Why Indian Parents Still Fear Creative Careers in 2025 — And How a New Generation Is Changing That",views.blog12,name='blog12'),
    path("Tamil Nadu Budget 2025–26: A Vision for Inclusive Growth, Social  Welfare, and Economic Stability",views.news7,name='news7'),
    path("Chandrayaan-4 vs. Chandrayaan-3: How India’s Next Moon Mission Is going to More Complex, Bold, and Groundbreaking",views.news8,name='news8'),
    path("India’s Electric Vehicle Revolution in 2025",views.blog13,name='blog13'),
    path("Mental Health Crisis in Gen Z: Why Are Young Adults More Depressed Than Ever?",views.blog14,name='blog14'),
    path("Tragic Ahmedabad Air India Crash Raises Urgent Questions on Flight Safety Protocols and Emergency Response in India in 2025",views.news9,name='news9'),
    path("Yuri Gagarin: The Brave Cosmonaut Who Became the First Human to Journey into Outer Space",views.biog,name='biog'),
    path("Discover the Top 7 Largest Deserts in the World: From Ice to Sand Wonders",views.top8,name='top8'),
    path("Top 5 Must-Watch Indian Web Series of 2025 That Completely Redefined Streaming Entertainment for Every Genre-Loving Viewer",views.top9,name='top9'),
    path("From Korean Dramas to Anime: How Global Streaming Trends Are Transforming Indian Entertainment Preferences in 2025",views.blog15,name='blog15'),
    path("How Social Media Is Quietly Rewiring the Teenage Brain: What Every Parent, Teen, and Teacher Should Know",views.blog16,name='blog16'),
    path("Why Overthinking Is the Real Villain in Modern Life — And How It Secretly Controls Our Daily Decisions",views.blog17,name='blog17'),
    path("Understanding the India’s Monsoon Season: How It Shapes the Economy, Agriculture, and the  Daily Life",views.blog18,name='blog18'),
    path("How the Kaveri River Continues to Shape the Culture, Agriculture, and Festival Traditions of Tamil Nadu in 2025",views.blog19,name='blog19'),
    path("How Iceland Lives With Fire and Ice: A Journey Through Volcanoes, Glaciers, and Human Resilience in 2025",views.blog20,name='blog20'),
    path("Top 5 Green Cities in the World That Are Leading the Way Toward Sustainable Urban Living",views.top10,name='top10'),
    path("The Role of Ayurveda and Modern Medicine: Can They Work Together for Better Health in the Modern World?",views.blog21,name='blog21'),
    path("Mental Health Awareness in the Digital Age: How to Stay Balanced, Focused, and Healthy While Living Online",views.blog22,name='blog22'),
    path("The Power of The Morning Routines: Simple habits to Boost your Day with Calm, Happy and Confidence",views.blog23,name='blog23'),
    path("The Dark Side of Social Media: How Digital Burnout is Quietly Affecting Our Mental Health, Relationships, and Productivity",views.blog24,name='blog24'),
    path("How Ocean Pollution Is Threatening Marine Life and What We Can Still Do to Save Our Seas",views.blog25,name='blog25'),
    path("Exploring the Future of Space Tourism: How Private Companies Are Making Space Travel Possible for Everyone in the Coming Decade",views.blog26,name='blog26'),
    path("The Possibility of Alien Life: Exploring Whether Humanity Is Truly Alone in the Vast Universe",views.blog27,name='blog27'),
    path("How Video Games Are Evolving from Entertainment to Education in the Modern Digital Era of 2025",views.blog28,name='blog28'),
    path("The Lost Art of Writing Letters: Why Handwritten Notes Still Matter in the Digital Age of Instant Messages and Emails",views.blog29,name='blog29'),
]
