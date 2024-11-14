from django.db import models

# Create your models here.


class BillingCompany(models.Model):
    id = models.BigAutoField(primary_key= True)
    name = models.CharField(max_length=100)
    contact = models.BigIntegerField(blank=True, null=True)
    notes = models.CharField(max_length=1024)

    def __str__(self):
        return f'{self.name} - {self.notes}'


class Bill(models.Model):
    id = models.BigAutoField(primary_key= True)
    due_date = models.DateTimeField(blank= True)
    payment_date = models.DateTimeField(blank=True, null= True)
    paymentAmount = models.FloatField(blank=True)
    company = models.ForeignKey(BillingCompany, on_delete=models.CASCADE)
    recurring = models.BooleanField(default= True)
    frequency = [
        ('monthly', 'Monthly'),
        ('annually', 'Annually'),
        ('semi-annually', 'Semi-Annually'),
        ('weekly', 'Weekly'),
        ('Daily','Daily')
    ]
    frequencyOfBilling = models.CharField(choices = frequency, default='monthly', max_length=200)
    def __str__(self):
        return f'{self.company.name} - ${self.paymentAmount} - {self.due_date}'

