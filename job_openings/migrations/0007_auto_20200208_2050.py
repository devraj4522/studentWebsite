# Generated by Django 3.0.2 on 2020-02-08 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_openings', '0006_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='updated',
        ),
        migrations.RemoveField(
            model_name='email',
            name='updated',
        ),
        migrations.AddField(
            model_name='email',
            name='post_title',
            field=models.CharField(default='', max_length=60),
        ),
    ]
