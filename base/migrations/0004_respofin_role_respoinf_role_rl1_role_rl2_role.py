# Generated by Django 4.0.5 on 2022-08-29 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_rcha_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='respofin',
            name='role',
            field=models.TextField(default='responsable financier'),
        ),
        migrations.AddField(
            model_name='respoinf',
            name='role',
            field=models.TextField(default='responsable informatique'),
        ),
        migrations.AddField(
            model_name='rl1',
            name='role',
            field=models.TextField(default='responsable logistique1'),
        ),
        migrations.AddField(
            model_name='rl2',
            name='role',
            field=models.TextField(default='responsable logistique2'),
        ),
    ]
