# Generated by Django 3.0.6 on 2020-06-15 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Electronics', '0019_order_recieve_bankname'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_recieve',
            name='PAYMENTMODE',
            field=models.CharField(default='PPI', max_length=50),
            preserve_default=False,
        ),
    ]