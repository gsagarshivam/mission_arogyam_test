# Generated by Django 3.1.3 on 2020-11-26 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heartcare', '0003_auto_20201126_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disease',
            name='desc',
            field=models.TextField(default=''),
        ),
    ]
