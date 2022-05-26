from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from agents.mixins import AgentAndLoginRequiredMixin
from docs.forms import DocsModelForm
from docs.models import Doc


class DocsListView(LoginRequiredMixin, ListView):
    template_name = 'docs/docs_list.html'
    context_object_name = 'docs'
    queryset = Doc.objects.all()


class DocsCreateView(AgentAndLoginRequiredMixin, CreateView):
    template_name = 'docs/docs_create.html'
    form_class = DocsModelForm
    success_url = '/docs'


class DocsDetailView(AgentAndLoginRequiredMixin, DetailView):
    template_name = 'docs/docs_detail.html'
    context_object_name = 'doc'
    queryset = Doc.objects.all()


class DocsUpdateView(AgentAndLoginRequiredMixin, UpdateView):
    template_name = 'docs/docs_update.html'
    model = Doc
    form_class = DocsModelForm
    success_url = '/docs'
    queryset = Doc.objects.all()


class DocsDeleteView(AgentAndLoginRequiredMixin, DeleteView):
    template_name = 'docs/docs_delete.html'
    model = Doc
    success_url = '/docs'

    def get_queryset(self):
        documents = self.request.user.userprofile
        return Doc.objects.filter(documents=documents)
