# Generated by Django 4.1.1 on 2023-04-15 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_order_trusty_alter_order_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='trusty',
        ),
        migrations.AddField(
            model_name='client',
            name='trusty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.client'),
        ),
        migrations.AlterField(
            model_name='order',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.client'),
        ),
    ]