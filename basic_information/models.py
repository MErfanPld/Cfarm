from django.db import models

# Create your models here.


class OwnerInformation(models.Model):
    first_name = models.CharField(max_length=150, verbose_name="نام")
    last_name = models.CharField(max_length=200, verbose_name="نام خانوادگی")
    mobile_number = models.CharField(
        max_length=11, verbose_name="شماره همراه")
    number_of_farms = models.IntegerField(
        blank=True, null=True, verbose_name="تعداد فارم")
    total_capacity = models.IntegerField(
        blank=True, null=True, default="0", verbose_name="ظرفیت کل")
    description = models.TextField(
        blank=True, null=True, verbose_name="توضیحات")

    def __str__(self):
        return self.last_name

    class Meta:
        verbose_name = "   اطلاعات مالک"
        verbose_name_plural = "   اطلاعات مالک"


class FarmInformation(models.Model):
    farm_name = models.CharField(max_length=100,  verbose_name="نام فارم")
    number_of_halls = models.IntegerField(
        blank=True, null=True, default="0", verbose_name="تعداد سالن")
    farm_capacity = models.IntegerField(
        blank=True, null=True, default="0", verbose_name="ظرفیت فارم ")
    description = models.TextField(
        blank=True, null=True, verbose_name="توضیحات")

    def __str__(self):
        return self.farm_name

    class Meta:
        verbose_name = "  اطلاعات فارم"
        verbose_name_plural = "  اطلاعات فارم"


class HallInformation(models.Model):
    hall_number = models.IntegerField(
        blank=True, null=True, default="0", verbose_name="شماره سالن")
    capacity = models.IntegerField(
        blank=True, null=True, default="0", verbose_name="ظرفیت")
    description = models.TextField(
        blank=True, null=True, verbose_name="توضیحات")

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = " اطلاعات سالن"
        verbose_name_plural = " اطلاعات سالن"


class StandardInformation(models.Model):
    # number_of_days = models. (شماره روز)
    number_of_casualties = models.IntegerField(
        blank=True, null=True, default="0", verbose_name="تعداد تلفات")
    elimination_number = models.IntegerField(
        blank=True, null=True, default="0", verbose_name="تعداد حذفی")
    toـcutـoffـtheـhead = models.IntegerField(
        blank=True, null=True, default="0", verbose_name="سربری")
    total_losses = models.IntegerField(
        blank=True, null=True, default="0", verbose_name="جمع تلفات")
    cumulative_losses = models.IntegerField(
        blank=True, null=True, default="0", verbose_name="تلفات تجمعی")
    consumed_seeds = models.IntegerField(
        blank=True, null=True, default="0", verbose_name="دانه مصرفی")
    collective_seeds = models.IntegerField(
        blank=True, null=True, default="0", verbose_name="دانه جمعی")
    per_capita_consumption = models.IntegerField(
        blank=True, null=True, default="0", verbose_name="سرانه مصرف")
    weight = models.IntegerField(
        blank=True, null=True, default="0", verbose_name="وزن")
    daily_weight_gain = models.IntegerField(
        blank=True, null=True, default="0", verbose_name="افزایش وزن روزانه")
    average_room_temperature = models.IntegerField(
        blank=True, null=True, default="0", verbose_name="میانگین دمای سالن")

    class Meta:
        verbose_name = "اطلاعات استاندارد"
        verbose_name_plural = "اطلاعات استاندارد"


# class VaccineProgramInformation(models.Model):
#     pass

    # class Meta:
    #     verbose_name = "اطلاعات واکسن "
    #     verbose_name_plural = "اطلاعات واکسن"


# class ShutdownProgramInformation(models.Model):
#     pass

    # class Meta:
    #     verbose_name = "اطلاعات خاموشی"
    #     verbose_name_plural = "اطلاعات خاموشی"
