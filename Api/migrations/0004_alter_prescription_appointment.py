# Generated by Django 3.2.19 on 2023-07-22 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0003_alter_prescription_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='Appointment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Api.appointmentlist'),
        ),
    ]
