# Generated by Django 4.1.7 on 2023-05-08 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenarios_api', '0014_workitem_alter_testcase_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workitem',
            name='id',
        ),
        migrations.AlterField(
            model_name='workitem',
            name='code',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
