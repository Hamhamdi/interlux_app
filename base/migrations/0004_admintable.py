# Generated by Django 4.0.5 on 2022-09-12 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_generaldtable_etape'),
    ]

    operations = [
        migrations.CreateModel(
            name='adminTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail_etape', models.CharField(max_length=200, null=True)),
                ('etape', models.IntegerField(default=1)),
            ],
        ),
    ]
