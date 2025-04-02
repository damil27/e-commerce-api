from django.urls import path
from . import views

# urlonfig File
urlpatterns = [
    path('hello/', views.say_hello),

]
