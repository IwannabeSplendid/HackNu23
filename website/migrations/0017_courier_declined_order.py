# Generated by Django 4.1.1 on 2023-04-15 21:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0016_alter_address_apartment_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='courier',
            name='declined_order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='declined_order', to='website.order'),
        ),
    ]