# Generated by Django 2.1.1 on 2018-09-21 22:59

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('indirizzo', models.CharField(max_length=50)),
                ('telefono', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True)),
                ('fax', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('sito_web', models.URLField()),
                ('nazionalita', models.CharField(max_length=50)),
                ('data_di_nascita', models.DateTimeField()),
            ],
        ),
    ]
