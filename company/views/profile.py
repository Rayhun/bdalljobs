from django.views.generic import DetailView
from jobs.models import Company


class CompanyProfile(DetailView):
    template_name = 'company/profile.html'
    model = Company

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        company = self.get_object()
        context['company_jobs'] = company.jobs.filter(job_status__code='03')
        return context
