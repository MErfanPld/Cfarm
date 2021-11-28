from django.db import models
from django.utils import timezone


class Cost(models.Model):
    cost_date = models.DateField(blank=True, null=True, verbose_name="تاریخ ")
    cost_title = models.CharField(
        blank=True, null=True, max_length=30, verbose_name="شرح هزینه")
    cost_type = models.CharField(
        blank=True, null=True, max_length=100, verbose_name="نوع هزینه")
    cost_amount = models.IntegerField(
        blank=True, null=True, verbose_name="مبلغ هزینه")
    cost_description = models.TextField(
        blank=True, null=True, max_length=300, verbose_name="توضیحات هزینه")

    def __str__(self):
        return self.cost_type

    class Meta:
        verbose_name = "مدیریت هزینه ها"
        verbose_name_plural = "  مدیریت هزینه ها"


class Income(models.Model):
    income_date = models.DateField(
        blank=True, null=True, verbose_name="تاریخ ")
    income_date = models.DateField(
        blank=True, null=True, verbose_name="تاریخ ")
    income_title = models.CharField(
        blank=True, null=True, max_length=30, verbose_name="شرح هزینه")
    income_type = models.CharField(
        blank=True, null=True, max_length=100, verbose_name="نوع هزینه")
    income_amount = models.IntegerField(
        blank=True, null=True, verbose_name="مبلغ هزینه")
    income_description = models.TextField(
        blank=True, null=True, max_length=300, verbose_name="توضیحات هزینه")

    class Meta:
        verbose_name = "مدیریت درآمدها"
        verbose_name_plural = "   مدیریت درآمدها"


class Debtor(models.Model):
    debtor_received = models.IntegerField(
        blank=True, null=True, verbose_name="دریافتی")
    debtor_to_borrow = models.IntegerField(
        blank=True, null=True, verbose_name="قرض گرفتن")
    debtor_title = models.CharField(
        blank=True, null=True, max_length=30, verbose_name="شرح ")

    class Meta:
        verbose_name = "بدهکار"
        verbose_name_plural = "بدهکار"


class Creditor(models.Model):
    creditor_payment = models.IntegerField(
        blank=True, null=True, verbose_name="پرداختی")
    creditor_to_lend = models.IntegerField(
        blank=True, null=True, verbose_name="قرض دادن")
    creditor_title = models.CharField(
        blank=True, null=True, max_length=30, verbose_name="شرح ")

    class Meta:
        verbose_name = "بستانکار"
        verbose_name_plural = " بستانکار"
