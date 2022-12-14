# Generated by Django 4.1.2 on 2022-10-09 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adevactes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('profile_pic', models.ImageField(upload_to='')),
                ('short_bio', models.CharField(max_length=500)),
                ('long_bio', models.CharField(max_length=1000)),
                ('advocate_years_exp', models.IntegerField()),
                ('youtube', models.CharField(max_length=100)),
                ('twitter', models.CharField(max_length=100)),
                ('github', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('logo', models.ImageField(upload_to='')),
                ('summery', models.CharField(max_length=1000)),
            ],
        ),
    ]
