# Generated by Django 4.1.7 on 2023-06-18 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenarios_api', '0011_testcase_actionable_steps'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='testcase',
            name='finished',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]