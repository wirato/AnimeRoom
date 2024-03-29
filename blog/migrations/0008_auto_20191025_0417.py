# Generated by Django 2.2.6 on 2019-10-24 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_service_icon02'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='link',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image'),
        ),
    ]
