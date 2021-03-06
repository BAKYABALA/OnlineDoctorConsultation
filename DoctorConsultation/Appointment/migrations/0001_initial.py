# Generated by Django 3.2.9 on 2021-11-26 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Doctor', '0001_initial'),
        ('Patient', '0002_remove_patient_patient'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TimeSlot', models.CharField(max_length=100)),
                ('SlotSession', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AppointmentDate', models.DateField()),
                ('AppointmentStatus', models.CharField(default='Pending', max_length=100)),
                ('AppointmentCreatedAt', models.DateTimeField(auto_now_add=True)),
                ('AppointmentClinic', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Doctor.clinic')),
                ('AppointmentDoctor', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Doctor.doctor')),
                ('AppointmentPatient', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Patient.patient')),
                ('AppointmentSlot', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Appointment.slot')),
            ],
        ),
    ]
