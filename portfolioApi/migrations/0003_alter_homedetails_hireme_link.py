# Generated by Django 4.0.2 on 2022-09-06 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioApi', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homedetails',
            name='hireMe_link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
