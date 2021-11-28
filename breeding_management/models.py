from django.db import models

# Create your models here.


class RecordDailyInformation(models.Model):
    pass

    class Meta:
        verbose_name = "ثبت اطلاعات روزانه"
        verbose_name_plural = "ثبت اطلاعات روزانه"


class DrugInformation_Vaccine_Trial(models.Model):

    # ? فیلدهای دارو
    date = models.DateField(blank=True, null=True, verbose_name="تاریخ ")
    medicine_name = models.CharField(max_length=100, verbose_name="نام دارو")
    consumption_seam = models.CharField(max_length=255, verbose_name="دز مصرف")
    description_of_drug_use = models.TextField(
        blank=True, null=True, verbose_name="توضیحات مصرف دارو")
    drug_performance_report = models.TextField(
        blank=True, null=True, verbose_name="گزارش عملکرد دارو")

    # ? فیلدهای واکسن
    date = models.DateField(blank=True, null=True, verbose_name="تاریخ ")
    vaccine_name = models.CharField(max_length=100,  verbose_name="نام واکسن")
    vaccine_report = models.TextField(
        blank=True, null=True, verbose_name="گزارش مصرف واکسن")

    # ? فیلدهای آزمایش
    date = models.DateField(blank=True, null=True, verbose_name="تاریخ ")
    test_name = models.CharField(max_length=100, verbose_name="نام آزمایش")
    number_of_samples = models.IntegerField(verbose_name="تعداد نمونه")
    upload_test_results = models.ImageField(upload_to='Trial/', verbose_name="اپلود نتیجه ازمایش")

    class Meta:
        verbose_name = "ثبت دارو – واکسن"
        verbose_name_plural = "ثبت دارو – واکسن"


class GeneralCondition(models.Model):
    pass

    def __str__(self):
        return

    class Meta:
        verbose_name = "وضعیت کلی"
        verbose_name_plural = "وضعیت کلی"


class Cortex(models.Model):
    pass

    def __str__(self):
        return

    class Meta:
        verbose_name = "کارتکس"
        verbose_name_plural = "کارتکس"
