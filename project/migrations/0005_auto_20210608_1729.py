# Generated by Django 3.2.4 on 2021-06-08 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_auto_20210608_1727'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='tasks',
        ),
        migrations.AddField(
            model_name='tasks',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project.projects'),
        ),
    ]
