from django.urls import path

from .views import *

app_name = 'leads'

urlpatterns = [
    path('', LeadListView.as_view(), name='lead_list'),
    path('<int:pk>/', LeadDetailView.as_view(), name='lead_detail'),
    path('create/', LeadCreateView.as_view(), name='lead_create'),
    path('<int:pk>/update/', LeadUpdateView.as_view(), name='lead_update'),
    path('<int:pk>/delete/', LeadDeleteView.as_view(), name='lead_delete'),
    path('<int:pk>/assign-agent/', AssignAgentView.as_view(), name='assign_agent'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('<int:pk>/category/', LeadCategoryUpdateView.as_view(), name='lead_category_update'),
    path('categories/create/', CategoryCreateView.as_view(), name='category_create'),
    path('categories/<int:pk>/update/', CategoryUpdateView.as_view(), name='category_update'),
    path('invitedleads/', InvitedLeadListView.as_view(), name='invited_lead_list'),
    path('invitedleads/create', InvitedLeadCreateView.as_view(), name='invited_lead_create'),
    path('invitedleads/<int:pk>', InvitedLeadDetailView.as_view(), name='invited_lead_detail'),
    path('invitedleads/<int:pk>/update', InvitedLeadUpdateView.as_view(), name='invited_lead_update'),
    path('invitedleads/<int:pk>/delete', InvitedLeadDeleteView.as_view(), name='invited_lead_delete'),
]
