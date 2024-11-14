# Generated by Django 3.2.25 on 2024-11-13 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BillingCompany',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('contact', models.BigIntegerField(blank=True)),
                ('notes', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('due_date', models.DateTimeField(blank=True)),
                ('paymentAmount', models.FloatField(blank=True)),
                ('recurring', models.BooleanField(default=True)),
                ('frequencyOfBilling', models.CharField(choices=[('monthly', 'Monthly'), ('annually', 'Annually'), ('semi-annually', 'Semi-Annually'), ('weekly', 'Weekly'), ('Daily', 'Daily')], default='monthly', max_length=200)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BillManagement.billingcompany')),
            ],
        ),
    ]