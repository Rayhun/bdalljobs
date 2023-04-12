from django.views.generic import TemplateView
from jobs.models import JobsPost, Company


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_jobs'] = JobsPost.objects.all().order_by('-id')[:8]
        context['govt_jobs'] = JobsPost.objects.filter(
            job_type__code='gj', is_active=True, job_status__code='03'
        ).order_by('-id')[:8]
        context['private_jobs'] = JobsPost.objects.filter(
            job_type__code='pj', is_active=True, job_status__code='03'
        ).order_by('-id')[:8]
        context['foreign_jobs'] = JobsPost.objects.filter(
            job_type__code='fj', is_active=True, job_status__code='03'
        ).order_by('-id')[:8]
        context['top_company'] = Company.objects.all()[:5]
        return context

