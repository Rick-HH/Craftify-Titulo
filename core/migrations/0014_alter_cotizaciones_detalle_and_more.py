# Generated by Django 4.2.5 on 2023-10-05 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_categoriaproductos_cotizaciones_marcaproductos_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizaciones',
            name='detalle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.detallecotizaciones'),
        ),
        migrations.AlterField(
            model_name='detallecotizaciones',
            name='id_cotizacion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.cotizaciones'),
        ),
    ]
