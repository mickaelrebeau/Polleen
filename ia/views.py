import pandas as pd
from django.shortcuts import render
from django.views.generic import ListView
from agents.mixins import AgentAndLoginRequiredMixin
from ia.models import Ia


class IaView(AgentAndLoginRequiredMixin, ListView):
    template_name = 'ia/ia.html'
    context_object_name = 'ia_list'
    data = pd.read_csv('ia/data/ia_data.csv')
    queryset = (Ia.objects.all(), data)
