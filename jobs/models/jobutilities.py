
import logging
from django.db import models

logger = logging.getLogger(__name__)


class JobType(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=25, null=True, blank=True)

    def __str__(self):
        return self.name


class JobStatus(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=25, null=True, blank=True)

    def __str__(self):
        return self.name


class EmploymentStatus(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=25, null=True, blank=True)

    def __str__(self):
        return self.name


class JobLevel(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=25, null=True, blank=True)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=255)
    employee = models.PositiveBigIntegerField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name
    
    @property
    def open_job(self):
        return self.jobs.filter(is_active=True, job_status__code='03').count()
    
    @property
    def employee_need(self):
        count = 0
        for obj in self.jobs.filter(is_active=True, job_status__code='03'):
            try:
                vacancy = int(obj.vacancy)
                count += vacancy
            except Exception as e:
                print(e)
        return count
