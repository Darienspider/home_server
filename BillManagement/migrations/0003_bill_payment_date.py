# Generated by Django 3.2.25 on 2024-11-13 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BillManagement', '0002_alter_billingcompany_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='payment_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
