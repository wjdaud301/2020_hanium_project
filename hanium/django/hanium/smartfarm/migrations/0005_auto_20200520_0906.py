# Generated by Django 2.2.12 on 2020-05-20 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartfarm', '0004_auto_20200518_0725'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ctl_values',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('fan_ctl', models.BooleanField()),
                ('water_ctl', models.BooleanField()),
                ('light_ctl', models.BooleanField()),
            ],
        ),
        migrations.RemoveField(
            model_name='data_values',
            name='fan_ctl',
        ),
        migrations.RemoveField(
            model_name='data_values',
            name='light_ctl',
        ),
        migrations.RemoveField(
            model_name='data_values',
            name='water_ctl',
        ),
    ]
