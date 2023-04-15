from django.views.generic import TemplateView
from jobs.models import JobsPost, EmploymentStatus, JobType


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employee_stats'] = EmploymentStatus.objects.all()
        context['job_type'] = JobType.objects.all()
        context['latest_jobs'] = JobsPost.objects.all().order_by('-id')[:8]
        govt_jobs = JobsPost.objects.filter(
            job_type__code='gj', is_active=True, job_status__code='03'
        ).order_by('-id')
        private_jobs = JobsPost.objects.filter(
            job_type__code='pj', is_active=True, job_status__code='03'
        ).order_by('-id')
        foreign_jobs = JobsPost.objects.filter(
            job_type__code='fj', is_active=True, job_status__code='03'
        ).order_by('-id')[:8]
        context['all_govt_jobs'] = govt_jobs
        context['all_private_jobs'] = private_jobs
        context['all_foreign_jobs'] = foreign_jobs
        context['govt_jobs'] = govt_jobs[:8]
        context['private_jobs'] = private_jobs[:8]
        context['foreign_jobs'] = foreign_jobs[:8]
        context['top_company'] = JobsPost.objects.all().distinct('company')
        return context

