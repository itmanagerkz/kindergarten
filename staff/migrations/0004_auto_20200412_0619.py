# Generated by Django 2.0.1 on 2020-04-12 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0003_auto_20200411_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='group/', verbose_name='фото групи'),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='tutor_position',
            field=models.CharField(choices=[('tutor', 'Вихователь'), ('assistant', 'Помічник'), ('psychologist', 'Психолог'), ('music', 'Муз керівник'), ('sport', 'Фіз рук')], max_length=15, verbose_name='посада'),
        ),
    ]
