# Generated by Django 3.1.3 on 2020-11-23 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kidneycare', '0005_auto_20201122_1723'),
    ]

    operations = [
        migrations.CreateModel(
            name='KidneycareVideo',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('content', models.CharField(default='', max_length=255)),
            ],
        ),
    ]
