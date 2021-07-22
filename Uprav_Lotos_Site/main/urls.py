
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('calculation',views.calculation, name='calculation'),
    path('contacts',views.contacts, name='contacts')



]

