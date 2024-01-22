# Generated by Django 5.0 on 2023-12-27 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopflee', '0028_availablebalance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='updatecashout',
            name='expense_source',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='updatecashin',
            name='income_source',
            field=models.CharField(max_length=250),
        ),
        migrations.DeleteModel(
            name='ExpenseSource',
        ),
        migrations.DeleteModel(
            name='IncomeSource',
        ),
    ]