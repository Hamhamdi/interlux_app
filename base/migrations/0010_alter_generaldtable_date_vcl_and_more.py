# Generated by Django 4.0.5 on 2022-09-29 13:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_alter_generaldtable_code_four_sage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generaldtable',
            name='date_VCL',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='generaldtable',
            name='delai_e2',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='generaldtable',
            name='delai_e3',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='generaldtable',
            name='delai_e4',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='generaldtable',
            name='delai_e5',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='generaldtable',
            name='statut_Imp',
            field=models.CharField(choices=[('', ''), ('En Negociation', 'En Negociation'), ('Confirmée fournée', 'Confirmée Fournée'), ('ex_c_payement', 'Ex_C_Payement'), ('en_preparation', 'En Preparation'), ('prelevee', 'Prelevee'), ('arrivee_maroc', 'Arrivee Maroc'), ('en_dedouanement', 'En Dedouanement'), ('liquide', 'Liquide'), ('en_entrepot', 'En Entrepot'), ('livree', 'Livree'), ('cloturee', 'Cloturee')], default='', max_length=20, null=True),
        ),
    ]
