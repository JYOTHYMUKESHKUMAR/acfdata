# Generated by Django 5.0 on 2024-03-10 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cashflow', '0005_rename_planned_balance_summary_balance'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dashboard',
            old_name='current_balance',
            new_name='balance',
        ),
    ]
