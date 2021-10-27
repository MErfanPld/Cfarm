# Generated by Django 3.2.8 on 2021-10-27 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_information', '0004_hallinformation'),
    ]

    operations = [
        migrations.CreateModel(
            name='StandardInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_casualties', models.IntegerField(blank=True, default='0', null=True, verbose_name='تعداد تلفات')),
                ('elimination_number', models.IntegerField(blank=True, default='0', null=True, verbose_name='تعداد حذفی')),
                ('toـcutـoffـtheـhead', models.IntegerField(blank=True, default='0', null=True, verbose_name='سربری')),
                ('total_losses', models.IntegerField(blank=True, default='0', null=True, verbose_name='جمع تلفات')),
                ('cumulative_losses', models.IntegerField(blank=True, default='0', null=True, verbose_name='تلفات تجمعی')),
                ('consumed_seeds', models.IntegerField(blank=True, default='0', null=True, verbose_name='دانه مصرفی')),
                ('collective_seeds', models.IntegerField(blank=True, default='0', null=True, verbose_name='دانه جمعی')),
                ('per_capita_consumption', models.IntegerField(blank=True, default='0', null=True, verbose_name='سرانه مصرف')),
                ('weight', models.IntegerField(blank=True, default='0', null=True, verbose_name='وزن')),
                ('daily_weight_gain', models.IntegerField(blank=True, default='0', null=True, verbose_name='افزایش وزن روزانه')),
                ('average_room_temperature', models.IntegerField(blank=True, default='0', null=True, verbose_name='میانگین دمای سالن')),
            ],
        ),
    ]