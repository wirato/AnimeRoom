# Generated by Django 2.2.6 on 2019-10-24 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20191025_0340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='images',
        ),
        migrations.AddField(
            model_name='service',
            name='icon02',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='image',
            field=models.ImageField(default='https://designshack.net/wp-content/uploads/background-design-trends-368x246.jpg', upload_to='images'),
        ),
    ]
