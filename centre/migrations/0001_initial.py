# Generated by Django 3.2.8 on 2022-01-22 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingCentre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(blank=True, max_length=1024)),
                ('price', models.CharField(blank=True, max_length=1024)),
                ('description', models.CharField(blank=True, max_length=1024)),
                ('photo', models.FileField(blank=True, upload_to='')),
            ],
        ),
    ]
