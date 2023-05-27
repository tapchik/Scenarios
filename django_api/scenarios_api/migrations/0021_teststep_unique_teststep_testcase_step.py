# Generated by Django 4.1.7 on 2023-05-16 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenarios_api', '0020_testsuite_unique_testsuite_workitem_version'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='teststep',
            constraint=models.UniqueConstraint(fields=('test_case', 'step'), name='unique_teststep_testcase_step'),
        ),
    ]
