# Generated by Django 4.1.4 on 2022-12-19 05:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_loan_date_due_alter_loan_date_out'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='loan',
            name='date_due',
            field=models.DateField(default=datetime.datetime(2023, 1, 2, 6, 46, 19, 702514)),
        ),
        migrations.AlterField(
            model_name='loan',
            name='date_out',
            field=models.DateField(default=datetime.datetime(2022, 12, 19, 6, 46, 19, 702514)),
        ),
    ]
