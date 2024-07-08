# Generated by Django 5.0.6 on 2024-07-08 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name_plural': 'Cities'},
        ),
        migrations.AddField(
            model_name='prediction',
            name='name',
            field=models.CharField(default='name', max_length=200),
            preserve_default=False,
        ),
    ]