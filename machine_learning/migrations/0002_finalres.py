# Generated by Django 4.2.5 on 2023-10-12 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machine_learning', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinalRes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('battery_power', models.IntegerField()),
                ('int_memory', models.IntegerField()),
                ('mobile_wt', models.IntegerField()),
                ('category', models.IntegerField()),
            ],
        ),
    ]
