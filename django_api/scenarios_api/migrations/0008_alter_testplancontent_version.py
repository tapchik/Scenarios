# Generated by Django 4.1.7 on 2023-06-09 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenarios_api', '0007_alter_testplancontent_version'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testplancontent',
            name='version',
            field=models.PositiveIntegerField(blank=True, default=1),
            preserve_default=False,
        ),
    ]
