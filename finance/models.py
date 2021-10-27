from django.db import models
from django.utils import timezone


class Cost(models.Model):
    cost_title = models.CharField(blank=True, null=True, max_length=30, verbose_name="شرح هزینه")
    cost_type = models.CharField(blank=True, null=True, max_length=100, verbose_name="نوع هزینه")
    cost_date = models.DateField(blank=True, null=True, auto_now_add=True, verbose_name="تاریخ ")
    cost_amount = models.IntegerField(blank=True, null=True, verbose_name="مبلغ هزینه")
    cost_description = models.TextField(blank=True, null=True, max_length=300, verbose_name="توضیحات هزینه")

    def __str__(self):
        return self.cost_type

    class Meta:
        verbose_name = " مالی"
        verbose_name_plural = " مالی"


class Income(models.Model):
    income_of_description = models.TextField(blank=True, null=True, max_length=300, verbose_name="توضیحات درامد")
    income_date = models.DateField(blank=True, null=True, auto_now_add=True, verbose_name="تاریخ ")
    income_amount = models.IntegerField(blank=True, null=True, verbose_name="مبلغ درامد")

    class Meta:
        verbose_name = "درآمد"
        verbose_name_plural = "درآمد"


class Debtor(models.Model):
    debtor_received = models.IntegerField(blank=True, null=True, verbose_name="دریافتی")
    debtor_to_borrow = models.IntegerField(blank=True, null=True, verbose_name="قرض گرفتن")

    class Meta:
        verbose_name = "بدهکار"
        verbose_name_plural = "بدهکار"


class Creditor(models.Model):
    creditor_payment = models.IntegerField(blank=True, null=True, verbose_name="پرداختی")
    creditor_to_lend = models.IntegerField(blank=True, null=True, verbose_name="قرض دادن")

    class Meta:
        verbose_name = "بستانکار"
        verbose_name_plural = "بستانکار"
