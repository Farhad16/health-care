# Generated by Django 3.0.7 on 2020-06-29 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_auto_20200629_0723'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hire',
            name='hospital',
        ),
    ]
