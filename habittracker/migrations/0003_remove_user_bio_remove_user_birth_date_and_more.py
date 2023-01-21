# Generated by Django 4.2a1 on 2023-01-19 16:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("habittracker", "0002_habit_record"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="bio",
        ),
        migrations.RemoveField(
            model_name="user",
            name="birth_date",
        ),
        migrations.RemoveField(
            model_name="user",
            name="location",
        ),
        migrations.AddField(
            model_name="habit",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="record",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="record",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]