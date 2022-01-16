from django.conf.urls import url 
from django.urls import path
from . import views

urlpatterns=[
    url('^$',views.home,name = 'home'),
    path('portfolio/',views.portfolio, name='portfolio'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('resume/', views.resume, name='resume'),
    path('search/',views.search,name='search_portfolio'),
    path('portfolio/details/<int:portfolio_id>',views.detail,  name='portfolio_details')
]