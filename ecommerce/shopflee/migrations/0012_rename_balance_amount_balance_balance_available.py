# Generated by Django 5.0 on 2023-12-13 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopflee', '0011_balance'),
    ]

    operations = [
        migrations.RenameField(
            model_name='balance',
            old_name='balance_amount',
            new_name='balance_available',
        ),
    ]
