# Generated by Django 5.0 on 2023-12-13 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopflee', '0005_alter_summary_cash_in_alter_summary_cash_out'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Summary',
        ),
    ]
