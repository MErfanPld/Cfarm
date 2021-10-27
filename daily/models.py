from django.db import models


# Create your models here.

class Daily_Informations(models.Model):
    date = models.DateField(verbose_name="تاریخ ")
    losses = models.IntegerField(verbose_name='تلفات جوجه', default=0)
    knockout = models.IntegerField(verbose_name='حذفیات جوجه', default=0)
    temprature_max = models.FloatField(verbose_name='کمترین دمای روز', null=True, blank=True)
    temprature_min = models.FloatField(verbose_name='بیشترین دمای روز', null=True, blank=True)
    seed = models.FloatField(verbose_name='دانه مصرفی در روز', null=True, blank=True)
    descriptions = models.CharField(null=False, blank=True, default=' ثبت نشده', max_length=200)

    class Meta:
        verbose_name = "ثبت اطلاعات روزانه"
        verbose_name_plural = "ثبت اطلاعات روزانه"

        indexes = [
            models.Index(fields=['date', ]),
        ]
