# Generated by Django 4.1.4 on 2022-12-22 18:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorial',
            name='attendancelist',
            field=models.CharField(default='[]', max_length=5500),
        ),
        migrations.AddField(
            model_name='tutorial',
            name='liveDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]