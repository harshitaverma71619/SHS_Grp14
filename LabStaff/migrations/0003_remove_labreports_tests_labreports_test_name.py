# Generated by Django 4.0.1 on 2022-03-29 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LabStaff', '0002_remove_labreports_id_alter_labreports_report_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='labreports',
            name='tests',
        ),
        migrations.AddField(
            model_name='labreports',
            name='test_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]