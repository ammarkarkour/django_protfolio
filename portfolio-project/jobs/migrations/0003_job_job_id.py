# Generated by Django 4.0.5 on 2022-07-02 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_job_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
