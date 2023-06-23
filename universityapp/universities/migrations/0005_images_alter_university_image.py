# Generated by Django 5.0.dev20230619181537 on 2023-06-23 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0004_rename_location_university_city_university_country_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.AlterField(
            model_name='university',
            name='image',
            field=models.ImageField(upload_to='universities/'),
        ),
    ]
