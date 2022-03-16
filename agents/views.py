import random

from django.core.mail import send_mail
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from agents.forms import AgentsModelForm
from agents.mixins import AgentAndLoginRequiredMixin
from leads.models import Agent


class AgentsListView(AgentAndLoginRequiredMixin, ListView):
    template_name = 'agents/agents_list.html'

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)


class AgentsCreateView(AgentAndLoginRequiredMixin, CreateView):
    template_name = 'agents/agents_create.html'
    form_class = AgentsModelForm
    success_url = '/agents'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_agent = True
        user.is_organiser = False
        user.set_password(f"{random.randint(0, 1000000)}")
        user.save()
        Agent.objects.create(
            user=user,
            organisation=self.request.user.userprofile,
        )
        send_mail(
            subject='You are invited to be an agent',
            message='You are invited to be an agent. Please click the link below to register',
            from_email='test@test.com',
            recipient_list=[user.email],
        )
        return super(AgentsCreateView, self).form_valid(form)


class AgentsDetailView(AgentAndLoginRequiredMixin, DetailView):
    template_name = 'agents/agents_detail.html'
    queryset = Agent.objects.all()
    context_object_name = 'agent'

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)


class AgentsUpdateView(AgentAndLoginRequiredMixin, UpdateView):
    template_name = 'agents/agents_update.html'
    model = Agent
    form_class = AgentsModelForm
    success_url = '/agents'

    def get_queryset(self):
        return Agent.objects.all()


class AgentsDeleteView(AgentAndLoginRequiredMixin, DeleteView):
    template_name = 'agents/agents_delete.html'
    model = Agent
    success_url = '/agents'

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)
