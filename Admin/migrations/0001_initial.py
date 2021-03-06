# Generated by Django 4.0.3 on 2022-03-29 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_id', models.IntegerField()),
                ('admin_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='StaffDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_id', models.IntegerField()),
                ('staff_name', models.CharField(max_length=100)),
                ('staff_dept', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TransactionDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('patient_id', models.IntegerField()),
                ('transaction_info', models.CharField(max_length=100)),
                ('transaction_status', models.CharField(max_length=100)),
                ('receipt_info', models.CharField(max_length=100)),
            ],
        ),
    ]
