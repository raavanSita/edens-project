# Generated by Django 3.1.6 on 2021-02-14 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0004_catogerytitle'),
    ]

    operations = [
        migrations.CreateModel(
            name='arrivalsContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('price', models.FloatField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
