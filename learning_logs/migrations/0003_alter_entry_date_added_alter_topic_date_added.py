# Generated by Django 5.1.2 on 2024-10-24 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0002_entry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
