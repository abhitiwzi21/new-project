# Generated by Django 2.1.1 on 2018-09-22 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_remove_employee_trans_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='trans_type',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
