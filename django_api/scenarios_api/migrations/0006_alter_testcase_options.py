# Generated by Django 4.1.7 on 2023-05-08 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scenarios_api', '0005_testcase_created_testcase_expected_result_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testcase',
            options={'verbose_name_plural': 'TestCases'},
        ),
    ]
