# Generated by Django 5.1.6 on 2025-03-24 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ModelApp', '0002_sales'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales',
            name='create_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='sales',
            name='update_at',
            field=models.DateTimeField(null=True),
        ),
    ]
