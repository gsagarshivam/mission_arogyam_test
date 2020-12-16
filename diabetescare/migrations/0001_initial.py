# Generated by Django 3.1.3 on 2020-12-01 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advisor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('advisor_name', models.CharField(max_length=50)),
                ('advisor_email', models.CharField(default='', max_length=70)),
                ('advisor_phone', models.CharField(default='', max_length=70)),
                ('messages', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=14)),
                ('slug', models.CharField(max_length=130)),
                ('timeStamp', models.DateTimeField(blank=True)),
                ('content', models.TextField()),
                ('image', models.ImageField(default='', upload_to='static/diabetescare/blog')),
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
            name='Disease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease_name', models.CharField(max_length=50)),
                ('category', models.CharField(default='', max_length=50)),
                ('subcategory', models.CharField(default='', max_length=50)),
                ('slug', models.CharField(default='', max_length=130)),
                ('content', models.TextField(default='')),
                ('desc', models.TextField(default='')),
                ('pub_date', models.DateField()),
                ('image', models.ImageField(default='', upload_to='static/diabetescare/disease')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evnet_title', models.CharField(max_length=50)),
                ('event_author', models.CharField(default='', max_length=50)),
                ('slug', models.CharField(default='', max_length=50)),
                ('desc', models.TextField(default='')),
                ('pub_date', models.DateField()),
                ('image', models.ImageField(default='', upload_to='static/diabetescare/event')),
            ],
        ),
        migrations.CreateModel(
            name='FilesAdmin',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('content', models.CharField(default='', max_length=255)),
                ('adminfile', models.FileField(default='', upload_to='media/diabetescare/pdf')),
                ('image', models.ImageField(default='', upload_to='static/diabetescare/pdf')),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slider_title', models.CharField(max_length=50)),
                ('pub_date', models.DateField()),
                ('image', models.ImageField(default='', upload_to='static/diabetescare/slider')),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testimonial_name', models.CharField(max_length=50)),
                ('content', models.TextField(default='')),
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