# Generated by Django 5.0 on 2024-01-07 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_booking', '0014_alter_user_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='avalible',
            field=models.BooleanField(default=True, verbose_name='Доступна'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='Cтаф статус'),
        ),
    ]