from django.urls import path
from app1 import views
urlpatterns = [
    path('',views.home),
    path('about',views.about),
    path('service',views.service),
    path('team',views.team),
    path('why',views.why),
]