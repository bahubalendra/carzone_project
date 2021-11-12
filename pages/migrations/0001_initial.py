# Generated by Django 3.2.9 on 2021-11-09 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=300)),
                ('last_name', models.CharField(max_length=300)),
                ('designation', models.CharField(max_length=300)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('facebook_link', models.URLField(max_length=300)),
                ('twitter_link', models.URLField(max_length=300)),
                ('google_plus_link', models.URLField(max_length=300)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]