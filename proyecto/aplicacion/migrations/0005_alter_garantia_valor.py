# Generated by Django 4.2.4 on 2023-08-30 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0004_garantia_fecha_final_garantia_fecha_inicial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='garantia',
            name='valor',
            field=models.DecimalField(decimal_places=2, max_digits=100),
        ),
    ]
