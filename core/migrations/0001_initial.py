# Generated by Django 5.0 on 2023-12-26 11:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='publicCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'publicCategory',
                'verbose_name_plural': 'publicCategories',
            },
        ),
        migrations.CreateModel(
            name='publicPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publicimage', models.ImageField(upload_to='')),
                ('publicdescription', models.TextField()),
                ('publiccategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.publiccategory')),
            ],
            options={
                'verbose_name': 'publicPhoto',
                'verbose_name_plural': 'publicPhotos',
            },
        ),
    ]
