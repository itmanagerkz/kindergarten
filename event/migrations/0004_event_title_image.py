# Generated by Django 2.0.1 on 2020-04-07 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_event_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='title_image',
            field=models.ImageField(blank=True, null=True, upload_to='event_title/%Y/%m/%d', verbose_name='фото обложки'),
        ),
    ]
