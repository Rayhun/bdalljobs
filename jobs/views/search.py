from django.views.generic import View
from django.shortcuts import render
from django.db.models import Q
# Local Import
from jobs.models import JobsPost, Skill, EmploymentStatus, JobType


class JobSearchView(View):
    template_name = 'jobs/search.html'
    model = JobsPost

    def get(self, request, *args):
        option = request.GET.get('options')
        job_type = request.GET.get('job_type')
        search = request.GET.get('q')
        get_skill = request.GET.get('skill')
        qs = self.model.objects.filter(is_active=True, job_status__code='03')
        if option:
            qs = qs.filter(employment_status__code=option)
        if job_type:
            qs = qs.filter(job_type__code=job_type)
        if search:
            try:
                skills = Skill.objects.filter(skill_name__icontains=search)
            except Exception as e:
                print(e)
                skills = None
            qs = qs.filter(
                Q(
                job_title__icontains=search) | Q(
                job_type__name=search) | Q(
                company__name=search) | Q(
                skills__in=skills
                )
            ).distinct('job_title')
        if get_skill:
            try:
                skills = Skill.objects.filter(skill_name=get_skill)
            except Exception as e:
                print(e)
                skills = None
            qs = qs.filter(skills__in=skills)
        employee_stats = EmploymentStatus.objects.all()
        all_job_type = JobType.objects.all()
        context = {
            'qs': qs, 'employee_stats': employee_stats, 'search': search,
            'option': option, 'job_type': job_type,
            'all_job_type': all_job_type
        }
        return render(request, self.template_name, context)
