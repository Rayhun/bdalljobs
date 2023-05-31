from django.views.generic import DetailView
from Core.models import User


class Profile(DetailView):
    template_name = 'profile/profile.html'
    model = User

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     user = self.get_object()
    #     return context
