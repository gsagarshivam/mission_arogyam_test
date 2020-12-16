# Generated by Django 3.1.3 on 2020-11-25 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArogyamSlider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slider_title', models.CharField(max_length=50)),
                ('pub_date', models.DateField()),
                ('image', models.ImageField(default='', upload_to='static/arogyam/slider')),
            ],
        ),
    ]
