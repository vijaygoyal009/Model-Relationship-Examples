# Generated by Django 5.1.1 on 2024-10-07 08:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="roll",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="ram",
                to="app.rollnumber",
            ),
        ),
    ]
