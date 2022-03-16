from django.urls import path, re_path

from .views import *

app_name = 'calendar'

urlpatterns = [
    path('', CalendarView.as_view(), name='calendar'),
    path('event/', event, name='event_new'),
    re_path(r'event/edit/(?P<event_id>\d+)/', event, name='event_edit'),
    path('event/delete/<int:pk>/', EventDeleteView.as_view(), name='event_delete'),
]
