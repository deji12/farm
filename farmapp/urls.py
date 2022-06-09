from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.home, name='home'),
    path('post-detail/<str:name>/', views.post_detail),
    path('contact/', views.contact, name='contact'),
    path('', views.landing, name='landing')
]