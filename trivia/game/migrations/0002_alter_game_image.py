# Generated by Django 3.2.7 on 2021-09-18 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='image',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
