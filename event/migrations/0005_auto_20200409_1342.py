# Generated by Django 2.0.1 on 2020-04-09 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_event_title_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': 'Подія', 'verbose_name_plural': 'Події'},
        ),
        migrations.AlterModelOptions(
            name='gallery',
            options={'verbose_name': 'Галерея', 'verbose_name_plural': 'Галереї'},
        ),
        migrations.AlterModelOptions(
            name='imagegallery',
            options={'verbose_name': 'Фото галереї', 'verbose_name_plural': 'Фото галереї'},
        ),
    ]
