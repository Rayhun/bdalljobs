from django.views.generic import TemplateView
from jobs.models import JobsPost


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jobs'] = JobsPost.objects.all()
        return context

