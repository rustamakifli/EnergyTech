# Generated by Django 4.2 on 2023-04-13 14:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appealicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'verbose_name': 'Appealicant',
                'verbose_name_plural': 'Appealicant',
            },
        ),
        migrations.CreateModel(
            name='AppealicantDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'verbose_name': 'Appealicant Day',
                'verbose_name_plural': 'Appealicant Days',
            },
        ),
        migrations.CreateModel(
            name='CompanyCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, db_index=True, help_text='Şəxsi VÖEN', max_length=30, null=True, verbose_name='Category name')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'verbose_name': 'Region',
                'verbose_name_plural': 'Regions',
            },
        ),
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_company', models.CharField(blank=True, db_index=True, help_text='Müəssinin adı', max_length=30, null=True, verbose_name='Müəssinin adı')),
                ('voen_code', models.CharField(blank=True, db_index=True, help_text='Şəxsi VÖEN', max_length=30, null=True, verbose_name='VÖEN Kod')),
                ('voen_activity', models.CharField(blank=True, db_index=True, help_text='Fəaliyyət növü', max_length=30, null=True)),
                ('appeal_no', models.CharField(blank=True, db_index=True, help_text='Müraciət No', max_length=30, null=True)),
                ('reyestr_num', models.CharField(blank=True, db_index=True, help_text='Reyestr number', max_length=30, null=True)),
                ('registr_num', models.CharField(blank=True, db_index=True, help_text='Registration number', max_length=30, null=True)),
                ('company_address', models.CharField(blank=True, db_index=True, help_text='Company Address', max_length=30, null=True)),
                ('tm_number', models.CharField(blank=True, db_index=True, help_text='TM number', max_length=30, null=True)),
                ('tm_x_coordination', models.CharField(blank=True, db_index=True, help_text='Tm X coordination', max_length=30, null=True)),
                ('tm_y_coordination', models.CharField(blank=True, db_index=True, help_text='TM y coordination', max_length=30, null=True)),
                ('length', models.CharField(blank=True, db_index=True, help_text='Lentgh', max_length=30, null=True)),
                ('more', models.CharField(blank=True, db_index=True, help_text='Add more', max_length=130, null=True)),
                ('appealicant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='appealicant_user', to='core.appealicant')),
                ('appleant_day', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='appealicant_day_user', to='core.appealicantday')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company_category', to='core.companycategory')),
                ('region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='region_object', to='core.region')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_applicant', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
