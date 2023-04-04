from django.db import models
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager
from .Abstract import CommonFieldModel
from .jobutilities import (
    JobType, Company, JobStatus, EmploymentStatus, JobLevel
)
from .categories import Category
from .skills import Skill


GENDER_CHOICES = (
    (1, 'Male'),
    (2, 'Female'),
    (3, 'Both'),
    (4, 'Others'),
)


class JobsPost(CommonFieldModel):
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name='jobs'
    )
    job_title = models.CharField(
        _('Job Title in English'), max_length=255
    )
    image = models.ImageField(null=True, blank=True, upload_to='job_images')
    slug = models.SlugField(unique=True, blank=True, null=True)
    vacancy = models.CharField(
        max_length=255, blank=True, null=True,
        help_text="Please Enter Vacancy Number",
    )
    published_date = models.DateField()
    deadline_date = models.DateField()
    gender = models.PositiveIntegerField(
        choices=GENDER_CHOICES, default=3
    )
    min_age = models.PositiveIntegerField(
        _('Minimum Age'), blank=True, null=True,
        help_text='Minimum Age (ex: 18)'
    )
    max_age = models.PositiveIntegerField(
        _('Maximum Age'), blank=True, null=True,
        help_text='Maximum Age (ex: 30)'
    )
    view_count = models.PositiveIntegerField(default=0)
    job_status = models.ForeignKey(
        JobStatus, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='jobs'
    )
    job_type = models.ForeignKey(
        JobType, on_delete=models.SET_NULL, null=True, related_name='jobs'
    )
    category = models.ManyToManyField(
        Category, related_name='jobs', blank=True
    )
    employment_status = models.ManyToManyField(
        EmploymentStatus, related_name='jobs', blank=True
    )
    job_level = models.ManyToManyField(
        JobLevel, related_name='jobs', blank=True
    )
    education = models.CharField(max_length=250, blank=True, null=True)
    experience = models.CharField(max_length=250, null=True)
    # Salary ==================================================================
    is_negotiable = models.BooleanField(default=False)
    salary = models.CharField(
        max_length=255, blank=True, null=True,
        help_text='Monthly Salary in BDT'
    )
    job_context = RichTextUploadingField(null=True, blank=True)
    skills = models.ManyToManyField(Skill, related_name='jobs', blank=True)
    job_skills = TaggableManager(
        help_text="A comma-separated list of skills.", blank=True
    )
    job_location = models.CharField(max_length=255, blank=True, null=True)
    apply_from_outside = models.BooleanField(
        default=True, blank=True, null=True
    )
    application_site_url = models.URLField(null=True, blank=True)
    application_with_email = models.EmailField(null=True, blank=True)
    send_cv_this_address = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.job_title

    def save(self, *args, **kwargs):
        if not self.slug:
            data = f"{self.job_title}-{self.pk}"
            self.slug = slugify(data)
        # if self.job_skills:
        #     for obj in self.job_skills.all():
        #         try:
        #             skill = obj.name.title()
        #             Skill.objects.get(skill_name=skill)
        #         except Exception as e:
        #             Skill.objects.create(skill_name=obj.name)
        super(JobsPost, self).save(*args, **kwargs)
