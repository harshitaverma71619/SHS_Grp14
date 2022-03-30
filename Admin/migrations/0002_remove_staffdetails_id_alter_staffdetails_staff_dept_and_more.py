# Generated by Django 4.0.1 on 2022-03-29 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staffdetails',
            name='id',
        ),
        migrations.AlterField(
            model_name='staffdetails',
            name='staff_dept',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='staffdetails',
            name='staff_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='staffdetails',
            name='staff_name',
            field=models.CharField(max_length=255),
        ),
    ]
