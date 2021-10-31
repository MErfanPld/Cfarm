from django.db import models
from django.utils import timezone


class Cost(models.Model):
    cost_title = models.CharField(
        blank=True, null=True, max_length=30, verbose_name="شرح هزینه")
    cost_type = models.CharField(
        blank=True, null=True, max_length=100, verbose_name="نوع هزینه")
    cost_date = models.DateField(null=True, blank=True, verbose_name="تاریخ ")
    cost_amount = models.IntegerField(
        blank=True, null=True, verbose_name="مبلغ هزینه")
    cost_description = models.TextField(
        blank=True, null=True, max_length=300, verbose_name="توضیحات هزینه")

    def __str__(self):
        return self.cost_type

    class Meta:
        verbose_name = "  هزینه"
        verbose_name_plural = "  هزینه"


class Income(models.Model):
    income_date = models.DateField(
        null=True, blank=True, verbose_name="تاریخ ")
    income_of_small_description = models.TextField(
        blank=True, null=True, max_length=300, verbose_name="شرح درآمد")
    income_type = models.FloatField(
        null=True, blank=True, verbose_name='نوع درآمد')
    income_the_amount = models.FloatField(
        null=True, blank=True, verbose_name='مقدار درآمد')
    income_price = models.CharField(
        max_length=500, blank=True, null=True, verbose_name='قیمت واحد')
    income_total = models.CharField(
        max_length=500, blank=True, null=True, verbose_name='جمع کل')
    income_of_description = models.TextField(
        blank=True, null=True, max_length=300, verbose_name="توضیحات")

    class Meta:
        verbose_name = " درآمد"
        verbose_name_plural = " درآمد"


class Debtor(models.Model):
    debtorـdate = models.DateField(
        null=True, blank=True, verbose_name="تاریخ ")
    debtor_of_small_description = models.TextField(
        blank=True, null=True, max_length=300, verbose_name="شرح ")
    debtor_the_amount = models.FloatField(
        null=True, blank=True, verbose_name='مبلغ')
    debtor_received = models.FloatField(
        blank=True, null=True, verbose_name="طرف حساب")
    debtor_description = models.TextField(
        blank=True, null=True, max_length=300, verbose_name="توضیحات ")

    class Meta:
        verbose_name = "بدهکار"
        verbose_name_plural = "بدهکار"


class Creditor(models.Model):
    creditorـdate = models.DateField(
        null=True, blank=True, verbose_name="تاریخ ")
    creditor_of_small_description = models.TextField(
        blank=True, null=True, max_length=300, verbose_name="شرح ")
    creditor_the_amount = models.FloatField(
        null=True, blank=True, verbose_name='مبلغ')
    creditor_received = models.FloatField(
        blank=True, null=True, verbose_name="طرف حساب")
    creditor_description = models.TextField(
        blank=True, null=True, max_length=300, verbose_name="توضیحات ")

    class Meta:
        verbose_name = "بستانکار"
        verbose_name_plural = "بستانکار"


class SellChicken(models.Model):
    class Meta:
        verbose_name = "فروش مرغ"
        verbose_name_plural = "فروش مرغ"
