# Generated by Django 3.2.22 on 2023-12-15 10:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20231208_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction_histroy',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
