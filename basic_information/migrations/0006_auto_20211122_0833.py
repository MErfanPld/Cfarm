# Generated by Django 3.2.8 on 2021-11-22 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_information', '0005_standardinformation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='farminformation',
            options={'verbose_name': 'اطلاعات فارم', 'verbose_name_plural': '  اطلاعات فارم'},
        ),
        migrations.AlterModelOptions(
            name='hallinformation',
            options={'verbose_name': 'اطلاعات سالن', 'verbose_name_plural': ' اطلاعات سالن'},
        ),
        migrations.AlterModelOptions(
            name='ownerinformation',
            options={'verbose_name': 'اطلاعات مالک', 'verbose_name_plural': '   اطلاعات مالک'},
        ),
        migrations.AlterModelOptions(
            name='standardinformation',
            options={'verbose_name': 'اطلاعات استاندارد', 'verbose_name_plural': 'اطلاعات استاندارد'},
        ),
    ]