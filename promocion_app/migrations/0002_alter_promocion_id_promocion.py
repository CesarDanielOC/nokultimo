# Generated by Django 5.1.2 on 2024-11-28 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promocion_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promocion',
            name='id_promocion',
            field=models.PositiveSmallIntegerField(primary_key=True, serialize=False),
        ),
    ]
