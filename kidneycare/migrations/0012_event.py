# Generated by Django 3.1.3 on 2020-11-24 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kidneycare', '0011_testimonial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evnet_title', models.CharField(max_length=50)),
                ('event_author', models.CharField(default='', max_length=50)),
                ('slug', models.CharField(default='', max_length=50)),
                ('desc', models.TextField(default='')),
                ('pub_date', models.DateField()),
                ('image', models.ImageField(default='', upload_to='static/kidneycare/disease')),
            ],
        ),
    ]
