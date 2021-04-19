# Generated by Django 3.1.7 on 2021-04-18 21:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eg', '0003_auto_20210417_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='likers',
            field=models.ManyToManyField(related_name='liker', to=settings.AUTH_USER_MODEL),
        ),
    ]
