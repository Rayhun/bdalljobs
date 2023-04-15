from django.views.generic import View
from django.shortcuts import render
from django.db.models import Q
# Local Import
from jobs.models import JobsPost, Skill, EmploymentStatus


class JobTypeView(View):
    template_name = 'jobs/job-type.html'
    model = JobsPost

    def get(self, request, code, *args):
        option = request.GET.get('options')
        search = request.GET.get('q')
        qs = self.model.objects.filter(
            is_active=True, job_status__code='03'
        )
        if code and not code == 'None':
            qs = qs.filter(job_type__code=code)
        if option:
            qs = qs.filter(employment_status__code=option)
        if search:
            try:
                skills = Skill.objects.filter(skill_name__icontains=search)
            except Exception as e:
                print(e)
                skills = None
            qs = qs.filter(
                Q(
                job_title__icontains=search) | Q(
                job_type__name=search) | Q (
                company__name=search) | Q (
                skills__in=skills
                )
            ).distinct('job_title')
        employee_stats = EmploymentStatus.objects.all()
        context = {
            'qs': qs, 'employee_stats': employee_stats, 'search': search,
            'option': option, 'job_type': code,
        }
        return render(request, self.template_name, context)
