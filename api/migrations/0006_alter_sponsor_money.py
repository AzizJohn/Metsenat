# Generated by Django 3.2.9 on 2021-12-13 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_sponsor_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='money',
            field=models.BigIntegerField(choices=[(1000000, '1 000 000'), (3000000, '3 000 000'), (5000000, '5 000 000'), (9000000, '9 000 000')], null=True),
        ),
    ]