# Generated by Django 2.2.12 on 2020-08-06 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0002_auto_20200806_0817'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addresses',
            old_name='address',
            new_name='email',
        ),
        migrations.RemoveField(
            model_name='addresses',
            name='name',
        ),
        migrations.AddField(
            model_name='addresses',
            name='user_id',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]