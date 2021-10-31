# Generated by Django 3.2.8 on 2021-10-31 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0010_auto_20211031_0708'),
    ]

    operations = [
        migrations.RenameField(
            model_name='creditor',
            old_name='date',
            new_name='creditorـdate',
        ),
        migrations.RenameField(
            model_name='debtor',
            old_name='date',
            new_name='debtorـdate',
        ),
        migrations.RemoveField(
            model_name='creditor',
            name='creditor_payment',
        ),
        migrations.RemoveField(
            model_name='creditor',
            name='creditor_to_lend',
        ),
        migrations.RemoveField(
            model_name='debtor',
            name='debtor_to_borrow',
        ),
        migrations.AddField(
            model_name='creditor',
            name='creditor_of_small_description',
            field=models.TextField(blank=True, max_length=300, null=True, verbose_name='شرح '),
        ),
        migrations.AddField(
            model_name='creditor',
            name='creditor_received',
            field=models.FloatField(blank=True, null=True, verbose_name='طرف حساب'),
        ),
        migrations.AddField(
            model_name='creditor',
            name='creditor_the_amount',
            field=models.FloatField(blank=True, null=True, verbose_name='مبلغ'),
        ),
        migrations.AddField(
            model_name='debtor',
            name='debtor_of_small_description',
            field=models.TextField(blank=True, max_length=300, null=True, verbose_name='شرح '),
        ),
        migrations.AddField(
            model_name='debtor',
            name='debtor_the_amount',
            field=models.FloatField(blank=True, null=True, verbose_name='مبلغ'),
        ),
        migrations.AlterField(
            model_name='debtor',
            name='debtor_received',
            field=models.FloatField(blank=True, null=True, verbose_name='طرف حساب'),
        ),
    ]