# Generated by Django 4.2.6 on 2023-10-12 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Beneficiary', '0002_alter_beneficiary_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beneficiary',
            name='Username',
            field=models.CharField(max_length=50),
        ),
    ]
