# Generated by Django 3.1.5 on 2021-09-27 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210927_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='decathlon_products',
            name='ProductSport',
            field=models.TextField(),
        ),
    ]