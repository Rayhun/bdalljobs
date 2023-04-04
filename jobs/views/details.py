from django.views.generic import TemplateView


class JobDetailsView(TemplateView):
    template_name = 'jobs/job_details.html'
