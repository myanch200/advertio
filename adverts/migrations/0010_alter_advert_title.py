# Generated by Django 3.2.4 on 2021-08-24 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adverts', '0009_wishlist_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='title',
            field=models.CharField(max_length=1000),
        ),
    ]