from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect


class AgentAndLoginRequiredMixin(AccessMixin):
    """
    CBV Mixin which verifies that the current user is authenticated and is an agent.
    """
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or request.user.is_agent == False:
            return redirect('/login')
        return super().dispatch(request, *args, **kwargs)