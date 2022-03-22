import random

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from docs.forms import DocsModelForm
from leads.models import Agent
from docs.models import Docs


class DocsListView(LoginRequiredMixin, ListView):
    template_name = 'docs/docs_list.html'

    def get_queryset(self):
        queryset = Docs.objects.all()
        return queryset


class DocsCreateView(LoginRequiredMixin, CreateView):
    template_name = 'docs/docs_create.html'
    form_class = DocsModelForm
    success_url = '/agents'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_agent = True
        user.is_organiser = False
        user.set_password(f"{random.randint(0, 1000000)}")
        user.save()
        return super().form_valid(form)


class DocsDetailView(LoginRequiredMixin, DetailView):
    template_name = 'agents/agents_detail.html'
    queryset = Agent.objects.all()
    context_object_name = 'agent'

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)


class DocsUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'docs/docs_update.html'
    model = Docs
    form_class = DocsModelForm
    success_url = '/docs'

    def get_queryset(self):
        return Agent.objects.all()


class DocsDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'docs/docs_delete.html'
    model = Docs
    success_url = '/docs'

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)
