# Generated by Django 2.1.1 on 2018-09-22 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0035_remove_employee_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='trans',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
