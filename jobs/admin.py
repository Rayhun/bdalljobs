from django.contrib import admin
from jobs import models


@admin.register(models.JobsPost)
class JobsPostAdmin(admin.ModelAdmin):
    list_display = [
        'company', 'job_title', 'vacancy', 'job_status', 
    ]


@admin.register(models.Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['skill_name', 'is_active']


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['parent', 'name']


@admin.register(models.JobLevel)
class JobLevelAdmin(admin.ModelAdmin):
    list_display = ['name', 'code']


@admin.register(models.EmploymentStatus)
class EmploymentStatusAdmin(admin.ModelAdmin):
    list_display = ['name', 'code']


@admin.register(models.JobStatus)
class JobStatusAdmin(admin.ModelAdmin):
    list_display = ['name', 'code']


@admin.register(models.JobType)
class JobTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'code']


@admin.register(models.Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'employee']
