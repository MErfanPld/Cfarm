# Generated by Django 3.2.8 on 2021-10-27 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OwnerInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150, verbose_name='نام')),
                ('last_name', models.CharField(max_length=200, verbose_name='نام خانوادگی')),
                ('mobile_number', models.CharField(max_length=11, verbose_name='شماره همراه')),
                ('number_of_farms', models.IntegerField(blank=True, null=True)),
                ('total_capacity', models.IntegerField(blank=True, default='0', null=True, verbose_name='ظرفیت کل')),
                ('description', models.TextField(blank=True, null=True, verbose_name='توضیحات')),
            ],
            options={
                'verbose_name': 'اطلاعات مالک',
                'verbose_name_plural': 'اطلاعات مالک',
            },
        ),
    ]
