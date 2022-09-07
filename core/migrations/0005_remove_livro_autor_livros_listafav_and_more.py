# Generated by Django 4.1.1 on 2022-09-07 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_livro_categoria_livro"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="livro",
            name="autor_livros",
        ),
        migrations.CreateModel(
            name="listafav",
            fields=[
                ("id_lista", models.AutoField(primary_key=True, serialize=False)),
                ("titulo_lista", models.CharField(max_length=100)),
                ("desc_lista", models.TextField()),
                (
                    "livros_lista",
                    models.ManyToManyField(related_name="lista_livro", to="core.livro"),
                ),
                (
                    "user_lista",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="Lista",
                        to="core.user",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="livro",
            name="autor_livros",
            field=models.ManyToManyField(related_name="livros", to="core.autor"),
        ),
    ]
