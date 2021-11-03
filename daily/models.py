from django.db import models


# Create your models here.

class Daily_Informations(models.Model):
    date = models.DateField(verbose_name="تاریخ ")
    losses = models.IntegerField(verbose_name='تلفات جوجه', default=0)
    knockout = models.IntegerField(verbose_name='حذفیات جوجه', default=0)
    temprature_max = models.FloatField(
        verbose_name='کمترین دمای روز', null=True, blank=True)
    temprature_min = models.FloatField(
        verbose_name='بیشترین دمای روز', null=True, blank=True)
    seed = models.FloatField(
        verbose_name='دانه مصرفی در روز', null=True, blank=True)
    price = models.CharField(max_length=500, blank=True,
                             null=True, verbose_name='قیمت واحد')
    weight = models.FloatField(
        max_length=500, blank=True, null=True, verbose_name='وزن')
    total = models.CharField(max_length=500, blank=True,
                             null=True, verbose_name='جمع کل')
    vaccine_registration = models.TextField(
        null=False, blank=True, default=' ثبت نشده', max_length=200, verbose_name='ثبت واکسن')
    weight_registration = models.TextField(
        null=False, blank=True, default=' ثبت نشده', max_length=200, verbose_name='ثبت وزن کشی')
    descriptions = models.TextField(
        null=False, blank=True, default=' ثبت نشده', max_length=200, verbose_name='توضیحات')

    class Meta:
        verbose_name = " ثبت اطلاعات روزانه"
        verbose_name_plural = " ثبت اطلاعات روزانه"

        indexes = [
            models.Index(fields=['date', ]),
        ]


class DrugRegistration(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ایدی')

    class Meta:
        verbose_name = "ثبت اطلاعات دارو"
        verbose_name_plural = "ثبت اطلاعات داور"


class VaccineRegistration(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ایدی')

    class Meta:
        verbose_name = "ثبت اطلاعات واکسن"
        verbose_name_plural = "ثبت اطلاعات واکسن"


class WeightRegistration(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ایدی')

    class Meta:
        verbose_name = "ثبت اطلاعات وزن کشی"
        verbose_name_plural = "ثبت اطلاعات وزن کشی"
