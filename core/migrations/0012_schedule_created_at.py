# Generated by Django 4.1.7 on 2023-05-18 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_schedule_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]