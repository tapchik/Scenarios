# Generated by Django 4.1.7 on 2023-05-08 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scenarios_api', '0009_alter_testcase_version'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testcase',
            old_name='tc_id',
            new_name='item',
        ),
    ]
