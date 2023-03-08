from django.db import models


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
