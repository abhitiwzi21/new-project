# Generated by Django 2.1.1 on 2018-09-21 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('transaction_id', models.IntegerField(default=5, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=500)),
                ('amount', models.IntegerField(default=10)),
            ],
        ),
    ]
