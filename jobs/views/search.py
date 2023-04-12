from django.views.generic import View
from django.shortcuts import render
from django.db.models import Q
# Local Import
from jobs.models import JobsPost, Skill


class JobSearchView(View):
    template_name = 'jobs/search.html'
    model = JobsPost

    def get(self, request, *args):
        option = request.GET.get('options')
        search = request.GET.get('q')
        get_skill = request.GET.get('skill')
        qs = self.model.objects.filter(is_active=True, job_status__code='03')
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
        if get_skill:
            try:
                skills = Skill.objects.filter(skill_name=get_skill)
            except Exception as e:
                print(e)
                skills = None
            qs = qs.filter(skills__in=skills)
        context = {
            'qs': qs,
        }
        return render(request, self.template_name, context)
