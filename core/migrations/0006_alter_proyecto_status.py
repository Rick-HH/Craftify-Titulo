# Generated by Django 4.2.5 on 2023-10-05 02:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_proyecto_equipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.statusporproyecto'),
        ),
    ]