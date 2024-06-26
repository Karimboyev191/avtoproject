# Generated by Django 5.0.4 on 2024-05-08 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pgapp', '0003_rename_hizmatlar_yonalishlar_xizmatlar'),
    ]

    operations = [
        migrations.CreateModel(
            name='TugallanganIshlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zakaz_id', models.IntegerField()),
                ('usta_id', models.IntegerField()),
                ('usta_haqqi', models.DecimalField(decimal_places=2, max_digits=10)),
                ('servis', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='diagnostikalar',
            name='usta_haqqi',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
