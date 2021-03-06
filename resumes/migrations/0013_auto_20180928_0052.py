# Generated by Django 2.1.1 on 2018-09-27 22:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resumes', '0012_auto_20180925_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cap_lingue',
            name='id_resume',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='resumes.Informazioni_Personali'),
        ),
        migrations.AlterField(
            model_name='cap_lingue',
            name='lettura',
            field=models.CharField(blank=True, choices=[('Elementare', 'Elementare'), ('Buono', 'Buono'), ('Eccellente', 'Eccellente')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='cap_lingue',
            name='nome_lingua',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cap_lingue',
            name='orale',
            field=models.CharField(blank=True, choices=[('Elementare', 'Elementare'), ('Buono', 'Buono'), ('Eccellente', 'Eccellente')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='cap_lingue',
            name='scrittura',
            field=models.CharField(blank=True, choices=[('Elementare', 'Elementare'), ('Buono', 'Buono'), ('Eccellente', 'Eccellente')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='esperienza_lavorativa',
            name='nome_datore',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='esperienza_lavorativa',
            name='tipo_azienda',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='esperienza_lavorativa',
            name='tipo_impiego',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='informazione_istruzione',
            name='materia_studio',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='informazione_istruzione',
            name='nome_formazione',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='informazione_istruzione',
            name='qualifica',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
