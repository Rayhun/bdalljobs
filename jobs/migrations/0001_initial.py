# Generated by Django 3.2.6 on 2023-04-04 04:56

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='jobs.category')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('employee', models.PositiveBigIntegerField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmploymentStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(blank=True, max_length=25, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='JobLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(blank=True, max_length=25, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='JobStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(blank=True, max_length=25, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='JobType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(blank=True, max_length=25, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=255, unique=True)),
                ('is_active', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['skill_name'],
            },
        ),
        migrations.CreateModel(
            name='JobsPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('order', models.IntegerField(blank=True, null=True, verbose_name='Order')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is Deleted')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created At')),
                ('last_updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Last Updated')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Deleted At')),
                ('job_title', models.CharField(max_length=255, verbose_name='Job Title in English')),
                ('image', models.ImageField(blank=True, null=True, upload_to='job_images')),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('vacancy', models.CharField(blank=True, help_text='Please Enter Vacancy Number', max_length=255, null=True)),
                ('published_date', models.DateField()),
                ('deadline_date', models.DateField()),
                ('gender', models.PositiveIntegerField(choices=[(1, 'Male'), (2, 'Female'), (3, 'Both'), (4, 'Others')], default=3)),
                ('min_age', models.PositiveIntegerField(blank=True, help_text='Minimum Age (ex: 18)', null=True, verbose_name='Minimum Age')),
                ('max_age', models.PositiveIntegerField(blank=True, help_text='Maximum Age (ex: 30)', null=True, verbose_name='Maximum Age')),
                ('view_count', models.PositiveIntegerField(default=0)),
                ('education', models.CharField(blank=True, max_length=250, null=True)),
                ('experience', models.CharField(max_length=250, null=True)),
                ('is_negotiable', models.BooleanField(default=False)),
                ('salary', models.CharField(blank=True, help_text='Monthly Salary in BDT', max_length=255, null=True)),
                ('job_context', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('job_location', models.CharField(blank=True, max_length=255, null=True)),
                ('apply_from_outside', models.BooleanField(blank=True, default=True, null=True)),
                ('application_site_url', models.URLField(blank=True, null=True)),
                ('application_with_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('send_cv_this_address', models.TextField(blank=True, null=True)),
                ('category', models.ManyToManyField(blank=True, related_name='jobs', to='jobs.Category')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='jobs.company')),
                ('created_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='jobs_jobspost_createdby', to=settings.AUTH_USER_MODEL)),
                ('deleted_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='jobs_jobspost_deleted', to=settings.AUTH_USER_MODEL)),
                ('employment_status', models.ManyToManyField(blank=True, related_name='jobs', to='jobs.EmploymentStatus')),
                ('job_level', models.ManyToManyField(blank=True, related_name='jobs', to='jobs.JobLevel')),
                ('job_skills', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of skills.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('job_status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='jobs', to='jobs.jobstatus')),
                ('job_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='jobs', to='jobs.jobtype')),
                ('skills', models.ManyToManyField(blank=True, related_name='jobs', to='jobs.Skill')),
                ('update_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='jobs_jobspost_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]