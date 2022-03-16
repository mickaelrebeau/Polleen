from django.urls import path

from .views import *

app_name = 'agents'

urlpatterns = [
    path('', AgentsListView.as_view(), name='agents_list'),
    path('<int:pk>/', AgentsDetailView.as_view(), name='agents_detail'),
    path('create/', AgentsCreateView.as_view(), name='agents_create'),
    path('<int:pk>/update/', AgentsUpdateView.as_view(), name='agents_update'),
    path('<int:pk>/delete/', AgentsDeleteView.as_view(), name='agents_delete'),
]