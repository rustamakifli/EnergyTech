# Generated by Django 4.2 on 2023-04-13 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_promocodeusing_promocode_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='promo_code',
            field=models.CharField(blank=True, db_index=True, help_text='Add more', max_length=6, null=True),
        ),
    ]