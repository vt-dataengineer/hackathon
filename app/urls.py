from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chat/', views.chat, name='chat'),
    path('generate/', views.generate_response, name='generate_terraform'),   # Correct view name
]

