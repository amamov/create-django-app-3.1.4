# Generated by Django 3.1.8 on 2021-05-09 15:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="avatar",
            field=models.ImageField(
                blank=True, help_text="48px x 48px", upload_to="users/profile/%Y/%m/%d"
            ),
        ),
        migrations.AddField(
            model_name="user", name="bio", field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="user",
            name="gender",
            field=models.CharField(
                blank=True,
                choices=[("M", "MALE"), ("F", "FEMALE"), ("O", "OTHER")],
                max_length=3,
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="phone_number",
            field=models.CharField(
                blank=True,
                max_length=12,
                validators=[
                    django.core.validators.RegexValidator("^010-?[1-9]\\d{3}-?\\d{4}$")
                ],
            ),
        ),
        migrations.AddField(
            model_name="user", name="website_url", field=models.URLField(blank=True),
        ),
    ]
