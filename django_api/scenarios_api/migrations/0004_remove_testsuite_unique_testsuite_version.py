# Generated by Django 4.1.7 on 2023-06-09 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scenarios_api', '0003_abstracttestsuite_testplan_testplancontent_user_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='testsuite',
            name='unique_testsuite_version',
        ),
    ]
