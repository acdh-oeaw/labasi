# Generated by Django 5.0.6 on 2024-06-24 13:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("places", "__first__"),
        ("vocabularies", "__first__"),
    ]

    operations = [
        migrations.CreateModel(
            name="Sign",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("sign_name", models.CharField(max_length=50)),
                (
                    "abz_number",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="ABZ Number"
                    ),
                ),
                (
                    "meszl_number",
                    models.CharField(
                        blank=True,
                        max_length=50,
                        null=True,
                        verbose_name="MesZL Number",
                    ),
                ),
                (
                    "image_1",
                    models.FileField(blank=True, null=True, upload_to="sign_img"),
                ),
                (
                    "image_2",
                    models.FileField(blank=True, null=True, upload_to="sign_img"),
                ),
            ],
            options={
                "ordering": ("sign_name",),
            },
        ),
        migrations.CreateModel(
            name="Tablet",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "text_reference",
                    models.CharField(
                        help_text="Eindeutiger Bezeichner des Textes", max_length=250
                    ),
                ),
                (
                    "title",
                    models.CharField(help_text="Titel der Instanz", max_length=250),
                ),
                (
                    "cdli_no",
                    models.CharField(
                        blank=True,
                        help_text="Nummer der Tafel in CDLI",
                        max_length=50,
                        verbose_name="CDLI no.",
                    ),
                ),
                (
                    "nabucco_no",
                    models.CharField(
                        blank=True,
                        help_text="Nummer der Tafel in NABUCCO",
                        max_length=50,
                        verbose_name="NABUCCO no.",
                    ),
                ),
                (
                    "museum_no",
                    models.CharField(
                        blank=True, max_length=50, verbose_name="Museum Number"
                    ),
                ),
                (
                    "place_information",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("external", "external"),
                            ("conjecture", "conjecture"),
                            ("internal", "internal"),
                            ("", "---------"),
                        ],
                        default="",
                        help_text="indicates the nature of the evidence supporting the reliability            or accuracy of the intervention or interpretation.                Suggested values include: 1] internal; 2] external; 3] conjecture",
                        max_length=50,
                    ),
                ),
                ("year", models.IntegerField(blank=True, null=True)),
                ("date_not_after", models.IntegerField(blank=True, null=True)),
                ("date_not_before", models.IntegerField(blank=True, null=True)),
                (
                    "babyloneian_time",
                    models.CharField(
                        blank=True, max_length=50, verbose_name="Babylonian time"
                    ),
                ),
                ("date_comment", models.TextField(blank=True, null=True)),
                (
                    "ductus",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("normal", "normal"),
                            ("slanting", "slanting"),
                            ("", "---------"),
                        ],
                        default="",
                        help_text="Gerader oder schräger Schriftduktus",
                        max_length=50,
                    ),
                ),
                (
                    "content",
                    models.TextField(
                        blank=True, help_text="Zusammenfassung d. Inhalts", null=True
                    ),
                ),
                (
                    "distinctive_protagonists",
                    models.CharField(
                        blank=True,
                        help_text="Im Text erwähnte Personen",
                        max_length=250,
                    ),
                ),
                (
                    "bibliography",
                    models.CharField(
                        blank=True,
                        help_text="Transliterationen oder Abdrucke ",
                        max_length=500,
                    ),
                ),
                (
                    "archive",
                    models.ForeignKey(
                        blank=True,
                        help_text="Archiv = Sammlung von Tafeln",
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="vocabularies.archive",
                    ),
                ),
                (
                    "dossier",
                    models.ForeignKey(
                        blank=True,
                        help_text="Unterkategorisierung v. Archiven",
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="vocabularies.dossier",
                    ),
                ),
                (
                    "period",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="vocabularies.period",
                    ),
                ),
                (
                    "place",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="places.place",
                    ),
                ),
                (
                    "region",
                    models.ForeignKey(
                        blank=True,
                        help_text="Fundregion",
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="vocabularies.region",
                    ),
                ),
                (
                    "scribe",
                    models.ForeignKey(
                        blank=True,
                        help_text="Schreiber",
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="vocabularies.scribe",
                    ),
                ),
                (
                    "text_type",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="vocabularies.texttype",
                    ),
                ),
            ],
            options={
                "ordering": ("title",),
            },
        ),
        migrations.CreateModel(
            name="Glyph",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("identifier", models.CharField(max_length=250)),
                ("reading", models.CharField(blank=True, max_length=250, null=True)),
                ("context", models.CharField(blank=True, max_length=250, null=True)),
                ("note", models.CharField(blank=True, max_length=250, null=True)),
                ("image", models.FileField(upload_to="glyph_img")),
                (
                    "sign",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="tablets.sign",
                    ),
                ),
                (
                    "tablet",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="tablets.tablet",
                    ),
                ),
            ],
            options={
                "ordering": ("-id",),
            },
        ),
        migrations.CreateModel(
            name="TabletImage",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.FileField(upload_to="tablet_img")),
                ("comment", models.TextField(blank=True, null=True)),
                (
                    "tablet",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="tablets.tablet"
                    ),
                ),
            ],
            options={
                "ordering": ("tablet",),
            },
        ),
    ]
