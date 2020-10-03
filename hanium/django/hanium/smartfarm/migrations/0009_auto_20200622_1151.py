# Generated by Django 2.2.12 on 2020-06-22 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartfarm', '0008_automaticsys_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='automaticsys',
            name='co2',
        ),
        migrations.RemoveField(
            model_name='automaticsys',
            name='hum_data',
        ),
        migrations.RemoveField(
            model_name='automaticsys',
            name='light_data',
        ),
        migrations.RemoveField(
            model_name='automaticsys',
            name='sm_data',
        ),
        migrations.RemoveField(
            model_name='automaticsys',
            name='tem_data',
        ),
        migrations.AddField(
            model_name='automaticsys',
            name='led_std',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='automaticsys',
            name='maxhum',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='automaticsys',
            name='minhum',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='automaticsys',
            name='pump_std',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
