# Generated by Django 5.0.4 on 2024-04-06 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='callevent',
            name='duration',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
