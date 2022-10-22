# Generated by Django 4.1.2 on 2022-10-22 09:59

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("elections", "0002_election_voters"),
    ]

    operations = [
        migrations.AddField(
            model_name="candidate",
            name="candidate_picture",
            field=models.ImageField(
                null=True,
                storage=django.core.files.storage.FileSystemStorage(
                    location="/media/photos"
                ),
                upload_to="",
            ),
        ),
    ]
