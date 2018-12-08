# Generated by Django 2.1.1 on 2018-09-22 11:08

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('resumes', '0007_cap_lingue'),
    ]

    operations = [
        migrations.CreateModel(
            name='Altre_Comp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descrizione_altre', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'verbose_name_plural': 'Altre Competenze',
            },
        ),
        migrations.CreateModel(
            name='Comp_Artistiche',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descrizione_artistiche', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'verbose_name_plural': 'Competenze Artistiche',
            },
        ),
        migrations.CreateModel(
            name='Comp_Organizzative',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descrizione_orga', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'verbose_name_plural': 'Competenze Organizzative',
            },
        ),
        migrations.CreateModel(
            name='Comp_Relazionali',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descrizione_rela', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'verbose_name_plural': 'Competenze Relazionali',
            },
        ),
        migrations.CreateModel(
            name='Comp_Tecniche',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descrizione_tecniche', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'verbose_name_plural': 'Competenze Tecniche',
            },
        ),
        migrations.AddField(
            model_name='informazioni_personali',
            name='madre_lingua',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='informazioni_personali',
            name='patenti',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='comp_tecniche',
            name='id_resume',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resumes.Informazioni_Personali'),
        ),
        migrations.AddField(
            model_name='comp_relazionali',
            name='id_resume',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resumes.Informazioni_Personali'),
        ),
        migrations.AddField(
            model_name='comp_organizzative',
            name='id_resume',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resumes.Informazioni_Personali'),
        ),
        migrations.AddField(
            model_name='comp_artistiche',
            name='id_resume',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resumes.Informazioni_Personali'),
        ),
        migrations.AddField(
            model_name='altre_comp',
            name='id_resume',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resumes.Informazioni_Personali'),
        ),
    ]
