# Generated by Django 3.2.8 on 2021-10-09 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_delete_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pin',
            name='pincategory',
            field=models.CharField(choices=[('Campus', 'CAMPUS LIFE'), ('Carrer', 'CARRER'), ('Culture', 'CULTURE'), ('Sports', 'GAMES'), ('Student', 'STUDENT'), ('Teacher', 'FACULTY')], default='Campus', max_length=100),
        ),
    ]
