# Generated by Django 4.2.5 on 2023-10-30 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='brand',
            field=models.CharField(choices=[('Hyundai', 'Hyundai'), ('Toyota', 'Toyota'), ('Ford', 'Ford'), ('Mahindra', 'Mahindra'), ('Skoda', 'Skoda'), ('Honda', 'Honda'), ('Tata', 'Tata'), ('Maruti Suzuki', 'Maruti Suzuki')], default='Tata', max_length=50),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='service',
            field=models.CharField(choices=[('AC Services', 'AC Services'), ('Car care Service', 'Car care Services'), ('Body Repair', 'Body Repair')], default='Body Repair', max_length=50),
        ),
    ]