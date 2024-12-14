# Generated by Django 5.0.6 on 2024-06-05 21:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Outflow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='outflows', to='inventory.inventory')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
