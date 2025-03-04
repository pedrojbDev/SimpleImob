# Generated by Django 5.0.6 on 2024-06-06 13:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('leads', '0001_initial'),
        ('modality', '0001_initial'),
        ('neighborhood', '0001_initial'),
        ('type', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('tel', models.CharField(max_length=30)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('requirement_rooms', models.IntegerField()),
                ('requirement_suites', models.IntegerField()),
                ('requirement_garage', models.IntegerField()),
                ('requirement_value', models.DecimalField(decimal_places=2, max_digits=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('lead', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='leads.leads')),
                ('requirement_modality', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='modality.modality')),
                ('requirement_neighborhood', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='neighborhood.neighborhood')),
                ('requirement_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='clients', to='type.type')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
