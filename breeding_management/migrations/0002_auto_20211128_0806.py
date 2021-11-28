# Generated by Django 3.2.8 on 2021-11-28 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('breeding_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DrugInformation_Vaccine_Trial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine_name', models.CharField(max_length=100, verbose_name='نام دارو')),
                ('consumption_seam', models.CharField(max_length=255, verbose_name='دز مصرف')),
                ('description_of_drug_use', models.TextField(blank=True, null=True, verbose_name='توضیحات مصرف دارو')),
                ('drug_performance_report', models.TextField(blank=True, null=True, verbose_name='گزارش عملکرد دارو')),
                ('vaccine_name', models.CharField(max_length=100, verbose_name='نام واکسن')),
                ('vaccine_report', models.TextField(blank=True, null=True, verbose_name='گزارش مصرف واکسن')),
                ('date', models.DateField(blank=True, null=True, verbose_name='تاریخ ')),
                ('test_name', models.CharField(max_length=100, verbose_name='نام آزمایش')),
                ('number_of_samples', models.IntegerField(verbose_name='تعداد نمونه')),
                ('upload_test_results', models.ImageField(upload_to='', verbose_name='اپلود نتیجه ازمایش')),
            ],
            options={
                'verbose_name': 'اطلاعات دارو ',
                'verbose_name_plural': 'اطلاعات دارو ',
            },
        ),
        migrations.DeleteModel(
            name='DrugInformation',
        ),
        migrations.DeleteModel(
            name='Vaccine',
        ),
        migrations.DeleteModel(
            name='Weightlifting',
        ),
    ]
