from django.urls import path
from . import views
from .views import PharmsAPIView,Pharms_de_gardeAPIView

urlpatterns = [
    #path('', views.home, name = 'home'),
    path('', PharmsAPIView.as_view()),
    path('garde/',Pharms_de_gardeAPIView.as_view()),
   
]
