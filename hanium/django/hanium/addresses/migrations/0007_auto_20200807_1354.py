# Generated by Django 2.2.12 on 2020-08-07 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0006_auto_20200806_2119'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addresses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('phone_number', models.CharField(max_length=13)),
                ('address', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
