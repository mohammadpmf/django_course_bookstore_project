# Generated by Django 4.1.7 on 2023-03-15 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_birth_date_customuser_nat_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='nat_id',
            field=models.CharField(blank=True, max_length=10, unique=True),
        ),
    ]