# Generated by Django 5.0.6 on 2024-06-11 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_alter_inventory_footage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='footage',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
