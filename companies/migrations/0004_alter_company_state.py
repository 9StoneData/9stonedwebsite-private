# Generated by Django 4.0.4 on 2022-06-02 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geos', '0002_rename_states_state'),
        ('companies', '0003_alter_company_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='State',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='geos.state'),
        ),
    ]
