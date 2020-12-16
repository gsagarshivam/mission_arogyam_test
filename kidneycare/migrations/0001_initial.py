# Generated by Django 3.1.3 on 2020-11-21 10:13

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


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
                ('image', models.ImageField(default='', upload_to='static/kidneycare/blog')),
                ('title2', models.CharField(default='', max_length=255)),
                ('content2', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('category', models.CharField(default='', max_length=50)),
                ('subcategory', models.CharField(default='', max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('desc', models.CharField(max_length=300)),
                ('pub_date', models.DateField()),
                ('image', models.ImageField(default='', upload_to='image/kidneycare')),
            ],
        ),
        migrations.CreateModel(
            name='BlogComment',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(default='', max_length=255)),
                ('useremail', models.CharField(default='', max_length=70)),
                ('userphone', models.CharField(default='', max_length=70)),
                ('comment', models.TextField(default='')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kidneycare.blogcomment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kidneycare.blog')),
            ],
        ),
    ]