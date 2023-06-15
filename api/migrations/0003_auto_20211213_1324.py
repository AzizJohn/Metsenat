# Generated by Django 3.2.9 on 2021-12-13 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_sponsor_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='contract',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='money',
            field=models.BigIntegerField(null=True),
        ),
        migrations.CreateModel(
            name='SponsorShip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money', models.BigIntegerField(null=True)),
                ('sponsor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='my_sponsorships', to='api.sponsor')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sponsorships', to='api.student')),
            ],
        ),
    ]