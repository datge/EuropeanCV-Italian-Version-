# Generated by Django 2.1.1 on 2018-12-07 23:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resumes', '0016_auto_20181007_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='altre_comp',
            name='id_resume',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='resumes.Informazioni_Personali'),
        ),
    ]
