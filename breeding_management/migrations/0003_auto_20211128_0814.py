# Generated by Django 3.2.8 on 2021-11-28 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('breeding_management', '0002_auto_20211128_0806'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='druginformation_vaccine_trial',
            options={'verbose_name': 'ثبت دارو – واکسن', 'verbose_name_plural': 'ثبت دارو – واکسن'},
        ),
        migrations.AlterField(
            model_name='druginformation_vaccine_trial',
            name='upload_test_results',
            field=models.ImageField(upload_to='Trial/', verbose_name='اپلود نتیجه ازمایش'),
        ),
    ]