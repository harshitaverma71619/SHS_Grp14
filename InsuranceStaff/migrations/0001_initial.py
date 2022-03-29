# Generated by Django 4.0.3 on 2022-03-29 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InsuranceClaimDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_id', models.IntegerField()),
                ('patient_firstname', models.CharField(default='fn', max_length=100)),
                ('patient_lastname', models.CharField(default='ln', max_length=100)),
                ('insurance_name', models.CharField(max_length=100)),
                ('claim_status', models.CharField(default='Pending', max_length=100)),
                ('claim_amt', models.IntegerField()),
            ],
        ),
    ]
