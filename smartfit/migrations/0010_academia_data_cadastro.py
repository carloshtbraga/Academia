# Generated by Django 4.2.3 on 2023-07-17 11:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("smartfit", "0009_alter_academia_endereco_alter_academia_telefone"),
    ]

    operations = [
        migrations.AddField(
            model_name="academia",
            name="data_cadastro",
            field=models.DateField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]