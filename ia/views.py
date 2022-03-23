from django.shortcuts import render
from django.views.generic import ListView
from agents.mixins import AgentAndLoginRequiredMixin


class IaView(AgentAndLoginRequiredMixin, ListView):
    pass
