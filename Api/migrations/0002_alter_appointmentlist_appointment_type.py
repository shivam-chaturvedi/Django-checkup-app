# Generated by Django 3.2.19 on 2023-06-16 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointmentlist',
            name='Appointment_type',
            field=models.CharField(choices=[('offline', 'Offline'), ('online', 'Online')], max_length=20),
        ),
    ]
