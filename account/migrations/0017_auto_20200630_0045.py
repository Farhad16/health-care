# Generated by Django 3.0.7 on 2020-06-29 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0016_remove_hire_hospital'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hire',
            old_name='dcotor_per_pic',
            new_name='prescribe_pic',
        ),
    ]
