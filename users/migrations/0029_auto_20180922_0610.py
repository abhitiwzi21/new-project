# Generated by Django 2.1.1 on 2018-09-22 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0028_remove_employee_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='address',
            field=models.CharField(default=None, max_length=500),
        ),
    ]
