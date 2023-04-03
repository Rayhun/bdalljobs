from django.views.generic import TemplateView
from Core.models import JobsPost


class IndexView(TemplateView):
    template_name = 'Core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_jobs = JobsPost.objects.all()
        context['top_jobs'] = all_jobs
        return context

