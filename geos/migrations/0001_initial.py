# Generated by Django 4.0.4 on 2022-06-02 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='States',
            fields=[
                ('Name', models.CharField(max_length=30)),
                ('State', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('Capital', models.CharField(max_length=50)),
            ],
        ),
    ]
