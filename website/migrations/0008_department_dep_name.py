# Generated by Django 4.1.1 on 2023-04-15 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_order_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='dep_name',
            field=models.CharField(default='Отделение', max_length=30),
        ),
    ]