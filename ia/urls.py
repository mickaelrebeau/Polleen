from django.urls import path

from .views import *

app_name = 'ia'

urlpatterns = [
    path('', IaView.as_view(), name='ia'),
]
