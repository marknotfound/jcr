# Generated by Django 4.0.10 on 2023-04-26 01:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discord', '0005_volunteeropportunity'),
    ]

    operations = [
        migrations.DeleteModel(
            name='VolunteerOpportunitySummary',
        ),
    ]