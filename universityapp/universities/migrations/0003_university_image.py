# Generated by Django 4.2.2 on 2023-06-21 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0002_university_description_university_domain'),
    ]

    operations = [
        migrations.AddField(
            model_name='university',
            name='image',
            field=models.ImageField(default='null', upload_to=''),
            preserve_default=False,
        ),
    ]
