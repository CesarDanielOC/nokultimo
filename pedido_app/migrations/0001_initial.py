# Generated by Django 5.1 on 2024-11-21 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id_pedido', models.PositiveSmallIntegerField(max_length=6, primary_key=True, serialize=False)),
                ('id_cliente', models.IntegerField()),
                ('fecha_pedido', models.CharField(max_length=100)),
                ('total_pedido', models.IntegerField()),
                ('estado_pedido', models.CharField(max_length=100)),
                ('metodo_pago', models.CharField(max_length=100)),
                ('direccion_envio', models.CharField(max_length=100)),
            ],
        ),
    ]
