# Generated by Django 2.0 on 2021-01-07 03:00

import case.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileupload',
            name='file_cover',
            field=models.ImageField(upload_to=case.utils.get_upload_path, verbose_name='文件封面'),
        ),
    ]