# Generated by Django 4.0.7 on 2022-09-13 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_product_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreview',
            name='review_rating',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=(1, '1')),
        ),
    ]
