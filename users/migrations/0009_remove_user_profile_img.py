# Generated by Django 4.0.1 on 2022-01-17 04:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_board_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='profile_img',
        ),
    ]
