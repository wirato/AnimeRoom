# Generated by Django 2.2.6 on 2019-10-24 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='image',
            field=models.ImageField(blank=True, upload_to='profile_image'),
        ),
    ]
