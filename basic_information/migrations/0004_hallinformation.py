# Generated by Django 3.2.8 on 2021-10-27 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_information', '0003_alter_farminformation_farm_capacity'),
    ]

    operations = [
        migrations.CreateModel(
            name='HallInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hall_number', models.IntegerField(blank=True, default='0', null=True, verbose_name='شماره سالن')),
                ('capacity', models.IntegerField(blank=True, default='0', null=True, verbose_name='ظرفیت')),
                ('description', models.TextField(blank=True, null=True, verbose_name='توضیحات')),
            ],
            options={
                'verbose_name': 'اطلاعات سالن',
                'verbose_name_plural': 'اطلاعات سالن',
            },
        ),
    ]
