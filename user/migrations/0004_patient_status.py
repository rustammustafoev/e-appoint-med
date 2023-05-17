# Generated by Django 4.1.7 on 2023-05-17 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_doctor_options_alter_patient_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='status',
            field=models.CharField(choices=[('IN', 'Under treatment'), ('OUT', 'Completed treatment')], default='IN', max_length=3),
        ),
    ]
