# Generated by Django 4.0.4 on 2022-06-02 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geos', '0004_alter_zip_population_with_in_10_miles_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zip',
            name='Population_with_in_100_miles',
            field=models.FloatField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='zip',
            name='Population_with_in_10_miles',
            field=models.FloatField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='zip',
            name='Population_with_in_1_miles',
            field=models.FloatField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='zip',
            name='Population_with_in_250_miles',
            field=models.FloatField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='zip',
            name='Population_with_in_25_miles',
            field=models.FloatField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='zip',
            name='Population_with_in_50_miles',
            field=models.FloatField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='zip',
            name='Population_with_in_5_miles',
            field=models.FloatField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='zip',
            name='irs_estimated_population',
            field=models.FloatField(blank=True, default=1, null=True),
        ),
    ]
