from django.urls import path
from.import views


urlpatterns = [
    path('', views.home, name='home-page'),
    path('demo', views.demo, name='demo-page'),
    path('getenglish', views.getEnglish, name='getEnglish'),
    path('geturdu', views.getUrdu, name='getUrdu'),
    path('contact', views.contact, name='contact'),
    path('hamnosys', views.hamnosys, name='hamnosys')
]
