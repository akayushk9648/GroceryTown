# Generated by Django 3.2.4 on 2023-09-18 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20230918_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='userid',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
