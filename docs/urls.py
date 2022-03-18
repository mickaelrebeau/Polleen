from django.urls import path

from .views import *

app_name = 'docs'

urlpatterns = [
    path('', DocsListView.as_view(), name='docs_list'),
    path('<int:pk>/', DocsDetailView.as_view(), name='docs_detail'),
    path('create/', DocsCreateView.as_view(), name='docs_create'),
    path('<int:pk>/update/', DocsUpdateView.as_view(), name='docs_update'),
    path('<int:pk>/delete/', DocsDeleteView.as_view(), name='docs_delete'),
]