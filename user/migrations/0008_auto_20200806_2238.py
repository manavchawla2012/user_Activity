# Generated by Django 3.1 on 2020-08-06 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20200806_2225'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='user_id',
            new_name='user',
        ),
    ]
