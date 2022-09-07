# Generated by Django 4.1.1 on 2022-09-07 00:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="autor",
            fields=[
                ("id_autor", models.AutoField(primary_key=True, serialize=False)),
                ("nome_autor", models.CharField(max_length=60)),
                ("desc_autor", models.TextField()),
                ("autor_nasc", models.DateField()),
                ("autor_falecimento", models.DateField(null=True)),
            ],
            options={
                "verbose_name_plural": "Autores",
            },
        ),
        migrations.CreateModel(
            name="categoria",
            fields=[
                ("id_categoria", models.AutoField(primary_key=True, serialize=False)),
                ("nome_categoria", models.CharField(max_length=30)),
                ("desc_categoria", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="editora",
            fields=[
                ("id_editora", models.AutoField(primary_key=True, serialize=False)),
                ("nome_editora", models.CharField(max_length=100)),
                ("desc_editora", models.TextField()),
                ("cnpj", models.PositiveIntegerField()),
                ("endereco_editora", models.CharField(max_length=150)),
                ("email_editora", models.EmailField(max_length=254)),
                ("senha_editora", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="user",
            fields=[
                ("id_usuario", models.AutoField(primary_key=True, serialize=False)),
                ("nome_usuario", models.CharField(max_length=60)),
                ("data_nasc", models.DateField()),
                ("telefone_user", models.PositiveIntegerField()),
                ("endereco_usuario", models.CharField(max_length=100)),
                ("cpf", models.PositiveIntegerField()),
                ("email_user", models.EmailField(max_length=254)),
                ("senha_user", models.CharField(max_length=20)),
                ("adm", models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name="livro",
            fields=[
                ("id_livro", models.AutoField(primary_key=True, serialize=False)),
                ("titulo_livro", models.CharField(max_length=100)),
                ("sinopse_livro", models.TextField()),
                ("qtd_paginas", models.PositiveIntegerField()),
                ("ano_lancamento", models.DateField()),
                ("url_compra", models.URLField()),
                (
                    "autor_livro",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="livros",
                        to="core.autor",
                    ),
                ),
                (
                    "editora_livro",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="livros",
                        to="core.editora",
                    ),
                ),
            ],
        ),
    ]
