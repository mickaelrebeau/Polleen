from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from docs.forms import DocsModelForm
from docs.models import Doc


class DocsListView(LoginRequiredMixin, ListView):
    template_name = 'docs/docs_list.html'

    def get_queryset(self):
        queryset = Doc.objects.all()
        return queryset


class DocsCreateView(LoginRequiredMixin, CreateView):
    template_name = 'docs/docs_create.html'
    form_class = DocsModelForm
    success_url = '/docs'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_agent = True
        user.is_organiser = False
        user.save()
        return super().form_valid(form)


class DocsDetailView(LoginRequiredMixin, DetailView):
    template_name = 'docs/docs_detail.html'
    context_object_name = 'docs'

    def get_queryset(self):
        queryset = Doc.objects.all()
        return queryset


class DocsUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'docs/docs_update.html'
    model = Doc
    form_class = DocsModelForm
    success_url = '/docs'

    def get_queryset(self):
        return Doc.objects.all()


class DocsDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'docs/docs_delete.html'
    model = Doc
    success_url = '/docs'

    def get_queryset(self):
        documents = self.request.user.userprofile
        return Doc.objects.filter(documents=documents)
