# Generated by Django 3.0.6 on 2020-06-06 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Electronics', '0004_mobiles'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('details', models.TextField()),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='Mobiles')),
                ('reviews', models.IntegerField(default=3)),
            ],
        ),
        migrations.DeleteModel(
            name='Mobiles',
        ),
    ]