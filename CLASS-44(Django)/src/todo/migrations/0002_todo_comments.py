# Generated by Django 5.1.5 on 2025-01-22 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='comments',
            field=models.TextField(blank=True, null=True),
        ),
    ]
