# Generated by Django 4.2.5 on 2023-11-02 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetodoPago',
            fields=[
                ('id_metodopago', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_metodo', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='cotizaciones',
            name='metodopago',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.metodopago'),
        ),
    ]