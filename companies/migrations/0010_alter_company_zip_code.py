# Generated by Django 4.0.4 on 2022-06-02 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0009_alter_company_zip_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='zip_code',
            field=models.CharField(default='tbd', max_length=12),
        ),
    ]
