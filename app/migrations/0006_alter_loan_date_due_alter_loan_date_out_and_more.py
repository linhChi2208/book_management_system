# Generated by Django 4.1.4 on 2022-12-19 20:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_borrower_user_alter_loan_date_due_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='date_due',
            field=models.DateField(default=datetime.datetime(2023, 1, 2, 21, 31, 33, 945271)),
        ),
        migrations.AlterField(
            model_name='loan',
            name='date_out',
            field=models.DateField(default=datetime.datetime(2022, 12, 19, 21, 31, 33, 945271)),
        ),
        migrations.AlterField(
            model_name='loan',
            name='date_returned',
            field=models.DateField(blank=True, null=True),
        ),
    ]
