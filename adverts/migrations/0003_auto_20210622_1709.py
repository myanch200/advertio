# Generated by Django 3.2.4 on 2021-06-22 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adverts', '0002_auto_20210622_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='advert',
            name='currency',
            field=models.CharField(choices=[('USD', 'USD'), ('EUR', 'EUR'), ('GBP', 'GBP'), ('BGN', 'BGN')], default='USD', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='advert',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
            preserve_default=False,
        ),
    ]
