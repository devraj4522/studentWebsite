# Generated by Django 3.0.2 on 2020-02-08 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job_openings', '0007_auto_20200208_2050'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-created',)},
        ),
    ]
