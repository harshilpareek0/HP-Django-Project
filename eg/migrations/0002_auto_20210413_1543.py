# Generated by Django 3.1.6 on 2021-04-13 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eg', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
