# Generated by Django 4.1.7 on 2023-06-09 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenarios_api', '0005_testplancontent_step_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testplancontent',
            options={'verbose_name_plural': 'TestPlanContents'},
        ),
        migrations.AddConstraint(
            model_name='testplancontent',
            constraint=models.UniqueConstraint(fields=('plan', 'step'), name='unique_step_for_testplan'),
        ),
    ]
