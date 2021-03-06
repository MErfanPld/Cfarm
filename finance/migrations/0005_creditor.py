# Generated by Django 3.2.8 on 2021-10-27 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0004_auto_20211027_0842'),
    ]

    operations = [
        migrations.CreateModel(
            name='Creditor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creditor_payment', models.IntegerField(blank=True, null=True, verbose_name='پرداختی')),
                ('creditor_to_lend', models.IntegerField(blank=True, null=True, verbose_name='قرض دادن')),
            ],
            options={
                'verbose_name': 'بستانکار',
                'verbose_name_plural': 'بستانکار',
            },
        ),
    ]
