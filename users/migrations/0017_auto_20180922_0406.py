# Generated by Django 2.1.1 on 2018-09-22 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_employee_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='trans_type',
            field=models.CharField(default=None, max_length=55),
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
