# Generated by Django 4.1 on 2022-08-23 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manage_project', '0002_rename_name_technologie_technologie_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='technologie',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='manage_project.technologie'),
            preserve_default=False,
        ),
    ]
