from django.urls import path,include
from Zoologico.views import HomeView

urlpatterns = [
    path('',HomeView.as_view(), name='home')
]