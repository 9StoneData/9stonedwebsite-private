# Generated by Django 4.0.4 on 2022-06-02 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='CLIENTa',
            new_name='CLIENT',
        ),
        migrations.AlterField(
            model_name='company',
            name='State',
            field=models.CharField(default='tbd', max_length=10),
        ),
    ]