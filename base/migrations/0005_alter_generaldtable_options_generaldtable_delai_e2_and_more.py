# Generated by Django 4.0.5 on 2022-09-19 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_admintable'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='generaldtable',
            options={'ordering': ['etape']},
        ),
        migrations.AddField(
            model_name='generaldtable',
            name='delai_e2',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='generaldtable',
            name='delai_e3',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='generaldtable',
            name='delai_e4',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='generaldtable',
            name='delai_e5',
            field=models.IntegerField(null=True),
        ),
    ]