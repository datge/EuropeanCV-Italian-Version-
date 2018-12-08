# Generated by Django 2.1.1 on 2018-09-22 00:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resumes', '0004_auto_20180922_0125'),
    ]

    operations = [
        migrations.CreateModel(
            name='Esperienza_Lavorativa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_da', models.DateField(blank=True, null=True)),
                ('data_a', models.DateField(blank=True, null=True)),
                ('nome_datore', models.CharField(max_length=100)),
                ('indirizzo_datore', models.CharField(blank=True, max_length=100, null=True)),
                ('tipo_azienda', models.CharField(max_length=100)),
                ('tipo_impiego', models.CharField(max_length=100)),
                ('principali_mansioni', models.CharField(blank=True, max_length=100, null=True)),
                ('id_resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resumes.Informazioni_Personali')),
            ],
            options={
                'verbose_name_plural': 'Esperienze Lavorative',
            },
        ),
    ]
