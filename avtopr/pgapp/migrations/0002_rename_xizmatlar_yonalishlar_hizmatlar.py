# Generated by Django 5.0.3 on 2024-04-18 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pgapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='yonalishlar',
            old_name='xizmatlar',
            new_name='hizmatlar',
        ),
    ]
