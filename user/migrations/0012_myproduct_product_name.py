# Generated by Django 3.2.4 on 2023-09-21 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_alter_myorders_order_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='myproduct',
            name='product_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
