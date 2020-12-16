# Generated by Django 3.1.3 on 2020-11-26 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heartcare', '0002_auto_20201126_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='', upload_to='static/heartcare/blog'),
        ),
        migrations.AlterField(
            model_name='disease',
            name='image',
            field=models.ImageField(default='', upload_to='static/heartcare/disease'),
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(default='', upload_to='static/heartcare/event'),
        ),
        migrations.AlterField(
            model_name='filesadmin',
            name='adminfile',
            field=models.FileField(default='', upload_to='media/heartcare/pdf'),
        ),
        migrations.AlterField(
            model_name='filesadmin',
            name='image',
            field=models.ImageField(default='', upload_to='static/heartcare/pdf'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='image',
            field=models.ImageField(default='', upload_to='static/heartcare/slider'),
        ),
    ]
