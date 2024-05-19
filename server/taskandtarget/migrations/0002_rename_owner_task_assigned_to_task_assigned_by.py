# Generated by Django 5.0.6 on 2024-05-19 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskandtarget', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='owner',
            new_name='assigned_to',
        ),
        migrations.AddField(
            model_name='task',
            name='assigned_by',
            field=models.CharField(choices=[('superadmin', 'superadmin'), ('admin', 'admin')], default='superadmin', max_length=20),
        ),
    ]
