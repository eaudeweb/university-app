# Generated by Django 4.2.2 on 2023-06-21 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("start", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="course", name="university",),
        migrations.AddField(
            model_name="university",
            name="courses",
            field=models.ManyToManyField(to="start.course"),
        ),
        migrations.AlterField(
            model_name="country", name="name", field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="level", name="name", field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="university",
            name="prestige",
            field=models.CharField(
                choices=[("low", "Low"), ("medium", "Medium"), ("high", "High")],
                default="medium",
                max_length=6,
            ),
        ),
    ]
