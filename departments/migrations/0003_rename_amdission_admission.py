# Generated by Django 4.2.4 on 2023-09-16 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
        ('departments', '0002_remove_amdission_status'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Amdission',
            new_name='Admission',
        ),
    ]
