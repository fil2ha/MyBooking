# Generated by Django 5.0 on 2023-12-22 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_booking', '0003_alter_booking_check_in_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='available',
        ),
        migrations.AddField(
            model_name='room',
            name='discription',
            field=models.TextField(default=True, verbose_name='Описание'),
        ),
    ]