# Generated by Django 3.2.2 on 2024-05-24 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0011_auto_20240521_2231'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='subtitle',
            field=models.CharField(default='Unknown', max_length=255),
        ),
    ]