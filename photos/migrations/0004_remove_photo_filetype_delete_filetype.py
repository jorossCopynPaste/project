# Generated by Django 5.0 on 2023-12-26 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_remove_photo2_category2_filetype_photo_filetype_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='filetype',
        ),
        migrations.DeleteModel(
            name='Filetype',
        ),
    ]
