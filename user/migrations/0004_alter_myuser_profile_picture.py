# Generated by Django 4.2 on 2023-04-14 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_remove_myuser_promo_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='profile_picture',
            field=models.ImageField(blank=True, default='images/Cool-Profile-Picture.webp', null=True, upload_to='profile_images'),
        ),
    ]
