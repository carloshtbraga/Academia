# Generated by Django 4.2.3 on 2023-07-17 01:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("smartfit", "0005_academia_nascimento"),
    ]

    operations = [
        migrations.AlterField(
            model_name="academia",
            name="plano",
            field=models.CharField(
                choices=[
                    ("Mensal", "Mensal"),
                    ("Semestral", "Semestral"),
                    ("Anual", "Anual"),
                ],
                default="Mensal",
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="academia",
            name="telefone",
            field=models.IntegerField(max_length=13),
        ),
    ]
