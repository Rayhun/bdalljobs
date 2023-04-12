from django.views.generic import DetailView
# Local Import
from jobs.models import JobsPost


class JobDetailsView(DetailView):
    template_name = 'jobs/details.html'
    model = JobsPost

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = self.model.objects.get(slug=self.kwargs['slug'])
        obj.view_count += 1
        obj.save()
        context['object'] = obj
        return context
