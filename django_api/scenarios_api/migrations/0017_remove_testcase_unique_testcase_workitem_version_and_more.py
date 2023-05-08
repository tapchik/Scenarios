# Generated by Django 4.1.7 on 2023-05-08 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenarios_api', '0016_alter_testcase_options_testcase_workitemm_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='testcase',
            name='unique_testcase_workitem_version',
        ),
        migrations.RenameField(
            model_name='testcase',
            old_name='workitemm',
            new_name='workitem',
        ),
        migrations.AddConstraint(
            model_name='testcase',
            constraint=models.UniqueConstraint(fields=('workitem', 'version'), name='unique_testcase_workitem_version'),
        ),
    ]