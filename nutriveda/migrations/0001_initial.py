# Generated by Django 3.1.3 on 2020-12-04 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=14)),
                ('slug', models.CharField(max_length=130)),
                ('timeStamp', models.DateTimeField(blank=True)),
                ('content', models.TextField()),
                ('image', models.ImageField(default='', upload_to='static/cancercare/blog')),
                ('title2', models.CharField(default='', max_length=255)),
                ('content2', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('subject', models.CharField(max_length=255, null=True)),
                ('mobileno', models.CharField(max_length=13, null=True)),
                ('messages', models.CharField(max_length=255)),
                ('createdon', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FilesAdmin',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('content', models.CharField(default='', max_length=255)),
                ('adminfile', models.FileField(default='', upload_to='media/cancercare/pdf')),
                ('image', models.ImageField(default='', upload_to='static/cancercare/pdf')),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slider_title', models.CharField(max_length=50)),
                ('pub_date', models.DateField()),
                ('image', models.ImageField(default='', upload_to='static/arogyaveda/slider')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('content', models.CharField(default='', max_length=255)),
            ],
        ),
    ]
