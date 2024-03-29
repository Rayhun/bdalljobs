# Generated by Django 3.2 on 2023-05-31 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20230404_1613'),
        ('Core', '0002_auto_20230404_1049'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_lavel', models.PositiveIntegerField(default=0, help_text='1 to 100')),
                ('skill_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='jobs.skill')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Core.profile')),
            ],
        ),
    ]
