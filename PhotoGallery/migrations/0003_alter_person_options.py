# Generated by Django 3.2.25 on 2024-11-13 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PhotoGallery', '0002_alter_images_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name_plural': 'People'},
        ),
    ]
