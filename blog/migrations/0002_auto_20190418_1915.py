# Generated by Django 2.1 on 2019-04-18 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='date_created',
            new_name='created_at',
        ),
    ]
