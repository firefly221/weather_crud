# Generated by Django 5.0.6 on 2024-07-08 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_prediction_votes'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='description',
            field=models.CharField(default='blank', max_length=600),
            preserve_default=False,
        ),
    ]