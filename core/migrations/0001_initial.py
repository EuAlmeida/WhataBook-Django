# Generated by Django 4.1.1 on 2022-09-29 17:26

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_cpf_cnpj.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="user",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                ("data_nasc", models.DateField(blank=True, null=True)),
                ("telefone_user", models.CharField(blank=True, max_length=11)),
                ("endereco_user", models.CharField(blank=True, max_length=100)),
                ("foto_perfil", models.ImageField(blank=True, upload_to="fotoperfil/")),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Usuarios",
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="autor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome_autor", models.CharField(max_length=60)),
                ("desc_autor", models.TextField()),
                ("autor_nasc", models.DateField()),
                ("autor_falecimento", models.DateField(blank=True, null=True)),
            ],
            options={
                "verbose_name_plural": "Autores",
            },
        ),
        migrations.CreateModel(
            name="categoria",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome_categoria", models.CharField(max_length=30)),
                ("desc_categoria", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="editora",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome_editora", models.CharField(max_length=100)),
                ("desc_editora", models.TextField()),
                ("cnpj", django_cpf_cnpj.fields.CNPJField(max_length=18)),
                ("endereco_editora", models.CharField(max_length=150)),
                ("email_editora", models.EmailField(max_length=254)),
                ("senha_editora", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="livro",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titulo_livro", models.CharField(max_length=100)),
                ("sinopse_livro", models.TextField()),
                ("qtd_paginas", models.PositiveIntegerField()),
                ("ano_lancamento", models.DateField()),
                ("url_compra", models.URLField()),
                ("capa_livro", models.ImageField(upload_to="images/")),
                (
                    "autor_livros",
                    models.ManyToManyField(related_name="livros", to="core.autor"),
                ),
                (
                    "categoria_livro",
                    models.ManyToManyField(related_name="livros", to="core.categoria"),
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
        migrations.CreateModel(
            name="resenha",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titulo_resenha", models.CharField(max_length=100)),
                ("desc_resenha", models.TextField()),
                (
                    "nota_resenha",
                    models.IntegerField(
                        choices=[
                            (1, "1 estrela"),
                            (2, "2 estrelas"),
                            (3, "3 estrelas"),
                            (4, "4 estrelas"),
                            (5, "5 estrelas"),
                        ]
                    ),
                ),
                (
                    "livro_resenha",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="resenha",
                        to="core.livro",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="listafav",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
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
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
