# Generated by Django 4.0.7 on 2022-09-11 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_order_total_after_discount_alter_order_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('Order Received', 'Order Recevied'), ('Order Processing', 'Order Processing'), ('on the way', 'on the way'), ('Order Complated', 'Order Complated'), ('Order Canceled', 'Order Canceled')], default=('Order Received', 'Order Recevied'), max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
    ]
