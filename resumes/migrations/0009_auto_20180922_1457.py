# Generated by Django 2.1.1 on 2018-09-22 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumes', '0008_auto_20180922_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informazioni_personali',
            name='data_di_nascita',
            field=models.DateField(),
        ),
    ]
