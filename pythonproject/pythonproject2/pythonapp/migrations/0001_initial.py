# Generated by Django 4.2 on 2023-05-09 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='places',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='pics')),
                ('desc', models.TextField()),
            ],
        ),
    ]