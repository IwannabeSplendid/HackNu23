# Generated by Django 4.1.1 on 2023-04-15 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_alter_client_iin_alter_courier_iin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='dep_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='order',
            name='description',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
