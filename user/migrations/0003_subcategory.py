# Generated by Django 3.2.4 on 2023-09-12 04:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_category_slider'),
    ]

    operations = [
        migrations.CreateModel(
            name='subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategory_name', models.CharField(max_length=100, null=True)),
                ('category_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.category')),
            ],
        ),
    ]
