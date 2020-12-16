# Generated by Django 3.1.3 on 2020-11-22 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kidneycare', '0002_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilesAdmin',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=14)),
                ('adminfile', models.FileField(default='', upload_to='media/kidneycare/pdf')),
            ],
        ),
    ]
