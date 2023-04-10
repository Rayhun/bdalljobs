from django.views.generic import TemplateView
from jobs.models import JobsPost


class IndexView(TemplateView):
    template_name = 'index.html'

