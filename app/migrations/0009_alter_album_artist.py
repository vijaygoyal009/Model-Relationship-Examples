# Generated by Django 5.1.1 on 2024-10-07 14:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0008_alter_album_artist"),
    ]

    operations = [
        migrations.AlterField(
            model_name="album",
            name="artist",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="auth",
                to="app.musician",
            ),
        ),
    ]
