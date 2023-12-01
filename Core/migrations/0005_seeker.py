# Generated by Django 3.2 on 2023-12-01 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0004_socialmedia_socialmedianame'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seeker',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
