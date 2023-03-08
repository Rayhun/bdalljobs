from django.contrib import admin

from Core import models


@admin.register(models.JobsPost)
class JobsPostModelAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'vacancy')


@admin.register(models.Skill)
class JobsPostModelAdmin(admin.ModelAdmin):
    list_display = ('skill_name', )


@admin.register(models.Category)
class JobsPostModelAdmin(admin.ModelAdmin):
    list_display = ('parent', 'name')


@admin.register(models.JobType)
class JobTypeModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')


@admin.register(models.JobStatus)
class JobStatusModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')


@admin.register(models.JobLevel)
class JobLevelModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')


@admin.register(models.EmploymentStatus)
class EmploymentStatusModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')


@admin.register(models.Company)
class CompanyModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'employee')
